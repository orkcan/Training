from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np
import json
import pyttsx3
import random
import speech_recognition as sr
import datetime
import requests
...

class PersonalAssistant:
    def __init__(self):
        ...
        # Define the maximum number of words to keep based on frequency
        self.max_num_words = 5000
        # Define maximum length of sequence
        self.max_len = 50
        # Initialize tokenizer
        self.tokenizer = Tokenizer(num_words=self.max_num_words)
        # Define a function map
        self.intent_map = {
            "add_event": self.add_event,
            "add_relationship": self.add_relationship,
            "learn": self.add_learning_progress,
            "daily_questions": self.ask_daily_question,
        }
        # Define a string to intent function mapping here as a dictionary
        self.string_to_intent = dict(
            [(i, intent) for i, intent in enumerate(self.intent_map.keys())]
        )
        ...

    def train_model(self):
        # Define a CNN model with multiple layers, and dropout for regularization
        model = Sequential([
            Embedding(self.max_num_words, 64, input_length=self.max_len),
            Conv1D(128, 5, activation='relu'),
            Conv1D(128, 5, activation='relu'),
            GlobalMaxPooling1D(),
            Dense(64, activation='relu'),
            Dropout(0.5),  # Add dropout layers to avoid overfitting
            Dense(64, activation='relu'),
            Dropout(0.5),
            Flatten(),  # Flatten the tensor output before feeding it into Dense layer
            Dense(len(self.intent_map.keys()), activation='softmax')
        ])
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Fit the model with the training examples (convert text into sequences for model consumption)
        examples = [ex for intent, exs in self.intents.items() for ex in exs]
        labels = [self.string_to_intent[intent] for intent, exs in self.intents.items() for ex in
                  exs]  # match class indices
        sequences = self.tokenizer.texts_to_sequences(examples)
        padded_sequences = pad_sequences(sequences, maxlen=self.max_len)
        model.fit(padded_sequences, np.array(labels), epochs=5)

        self.intent_classifier = model

    ...

    def start_listening(self):
        ...
        while self.is_listening:
            user_input = self.voice_input()
            if not user_input:
                continue

            # Tokenize and pad the user input
            processed_input = self.tokenizer.texts_to_sequences([user_input])
            padded_input = pad_sequences(processed_input, maxlen=self.max_len)

            # Predict the intent
            intent_prediction = np.argmax(self.intent_classifier.predict(padded_input))

            # Perform action associated with predicted intent
            action = self.intent_map[self.string_to_intent[intent_prediction]]
            action(user_input)  # execute the function mapped to the predicted intent

        ...
