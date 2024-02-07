import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.model_selection import train_test_split

# Pip install these if not present.
# Pretrained model has to exist on HuggingFace's Model Hub.
PRETRAINED_MODEL = 'bert-base-uncased'

tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL)
model = AutoModelForSequenceClassification.from_pretrained(PRETRAINED_MODEL)

# Load the data. I'll assume ynacc's comments data as default.
# sentences: list of sentences
# labels: list of intent_classes (0 or 1; you may need to modify labels to numeric format)
sentences = ['the weather is good today', 'set alarm at 7 am', ...]
labels = [0 , 1 ,...]

sentences_train, sentences_test, labels_train, labels_test = train_test_split(sentences, labels, test_size=0.2, random_state=42)

inputs = tokenizer(sentences_train, return_tensors='pt', truncation=True, padding=True)
outputs = model(**inputs, labels=torch.tensor(labels_train))

# Access the loss here using outputs.loss
loss = outputs.loss
loss.backward()

# Now you can use your favorite optimizer to update the weights with loss

# Interactive
while True:
    command = input('Ask a yes/no question: ')
    prediction = model.predict([command])[0]
    if prediction == 'ynQuestion':
        answer = random.choice(['Yes', 'No'])
        print(answer)
    else:
        print('Sorry, I did not understand the question. Could you please ask a yes or no question?')import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.model_selection import train_test_split

# Pip install these if not present.
# Pretrained model has to exist on HuggingFace's Model Hub.
PRETRAINED_MODEL = 'bert-base-uncased'

tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_MODEL)
model = AutoModelForSequenceClassification.from_pretrained(PRETRAINED_MODEL)

# Load the data. I'll assume ynacc's comments data as default.
# sentences: list of sentences
# labels: list of intent_classes (0 or 1; you may need to modify labels to numeric format)
sentences = ['the weather is good today', 'set alarm at 7 am', ...]
labels = [0 , 1 ,...]

sentences_train, sentences_test, labels_train, labels_test = train_test_split(sentences, labels, test_size=0.2, random_state=42)

inputs = tokenizer(sentences_train, return_tensors='pt', truncation=True, padding=True)
outputs = model(**inputs, labels=torch.tensor(labels_train))

# Access the loss here using outputs.loss
loss = outputs.loss
loss.backward()

# Now you can use your favorite optimizer to update the weights with loss

# Interactive