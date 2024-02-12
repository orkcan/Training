#analyzer.py
import time
import os
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from transformers import BertTokenizerFast, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


class EmotionDataset(torch.utils.data.Dataset):
    def __init__(self, input_ids, attention_masks, labels):
        self.input_ids = input_ids
        self.attention_masks = attention_masks
        self.labels = labels

    def __getitem__(self, idx):
        item = {'input_ids': self.input_ids[idx],
                'attention_mask': self.attention_masks[idx],
                'labels': self.labels[idx]}
        return item

    def __len__(self):
        return len(self.labels)


class BERTAnalyzer:
    def __init__(self, model_path='model.pt', data_path='emotions_dataset_kaggle.csv'):  # define path to your dataset here
        self.data_path = data_path  # set attribute
        self.tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased', do_lower_case=True)
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=6)
        self.model_path = model_path
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.le = LabelEncoder()

        # Check if the model has been trained already
        if os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path))
        else:
            # If no trained model, initiate the training process
            dataset = pd.read_csv(self.data_path)
            input_ids, attention_masks, labels = self.preprocess(dataset)
            self.train(input_ids, attention_masks, labels, epochs=3)
            # Save the model
            torch.save(self.model.state_dict(), self.model_path)

        self.model.to(self.device)

    def preprocess(self, dataset):
        # Assuming the dataset is in the form of a DataFrame with 'text' and 'emotion' columns
        text = dataset['text'].tolist()
        self.le.fit(dataset['label'])
        labels = self.le.transform(dataset['label']).tolist()

        # Encode our concatenated data
        encodings = self.tokenizer(text, truncation=True, padding=True)

        # splitting encodings to input_ids and attention_mask separately and convert them to tensors
        input_ids = torch.tensor(encodings['input_ids'])
        attention_masks = torch.tensor(encodings['attention_mask'])
        labels = torch.tensor(labels)

        return input_ids, attention_masks, labels  # <- returning the separated lists

    def train(self, input_ids, attention_masks, labels, epochs):
        train_inputs, val_inputs, train_masks, val_masks, train_labels, val_labels = train_test_split(input_ids,
                                                                                                      attention_masks,
                                                                                                      labels,
                                                                                                      random_state=42,
                                                                                                      test_size=0.2)

        # DataLoader are used for efficiently loading the data in chunks
        train_data = EmotionDataset(train_inputs, train_masks, train_labels)
        train_loader = DataLoader(train_data, batch_size=16)
        total_batches = len(train_loader)

        optimizer = optim.AdamW(self.model.parameters(), lr=1e-5)

        # Training loop
        self.model.train()
        for epoch in range(epochs):
            print(f'\n Epoch: {epoch}')
            for i, batch in enumerate(train_loader):
                start_time = time.time()
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)
                outputs = self.model(input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs[0]
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
                end_time = time.time()
                time_for_batch = end_time - start_time

                # print status every 100 batches
                if i % 100 == 0:
                    print(f'\tBatch: {i}, Loss: {loss.item()}, Time for batch: {time_for_batch} seconds')
                    remaining_batches = total_batches - i

                    # estimate remaining time for this epoch
                    time_for_remaining_batches = remaining_batches * time_for_batch
                    print(
                        f'\tEstimated time left for this epoch: {time_for_remaining_batches} seconds (~{time_for_remaining_batches / 60} minutes)')

        torch.save(self.model.state_dict(), self.model_path)
    def predict(self, text):
        text = [text]
        # Encode the text
        encoded_sent = self.tokenizer(text, truncation=True, padding=True, return_tensors="pt")
        input_ids = encoded_sent['input_ids'].to(self.device)
        attention_mask = encoded_sent['attention_mask'].to(self.device)

        # Get the model's predictions
        self.model.eval()
        with torch.no_grad():
            logits = self.model(input_ids, attention_mask=attention_mask)

        # Get the predicted intent
        predicted_intent = np.argmax(logits[0].cpu()).item()
        predicted_intent = self.le.inverse_transform([predicted_intent])

        return predicted_intent[0]