import spacy
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pyttsx3
import datetime
import requests
import csv
import speech_recognition as sr
import json
import random

class PersonalAssistant:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.data = {"events": [], "relationships": [], "learning": [], "daily_questions": []}
        self.model = None
        self.engine = pyttsx3.init()
        self.is_listening = False
        # define known intents
        self.intents = {
            "add_event": ["add event", "create event", "new event"],
            "add_relationship": ["add relationship", "create relationship", "new relationship"],
            "learn": ["learn", "learning"],
            "daily_questions": ["ask daily questions", "daily questions"],
            "train_model": ["train model", "model training"],
            "search": ["search", "find", "lookup"],
            "stop": ["stop listening", "stop"],
            "ask_question": ["ask me a question", "can you ask me a question"]
        }
        # load spacy model
        self.spacy_model = spacy.load("en_core_web_lg")
    def save_to_file(self):
        with open("data.json", "w") as f:
            json.dump(self.data, f)

    def voice_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query

        except Exception as e:
            print(e)
            print("Unable to recognize your voice.")
            return ""

    def add_event(self, event_text):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["events"].append({"text": event_text, "date": date})

    def add_relationship(self, relationship_text):
        self.data["relationships"].append({"text": relationship_text})

    def add_learning_progress(self, subject, progress_text):
        self.data["learning"].append({"subject": subject, "text": progress_text})

    def add_daily_question_answer(self, question, answer):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.data["daily_questions"].append({"question": question, "answer": answer, "date": date})

    def ask_daily_question(self):
        questions = [
            "How did your day go?",
            "What did you learn today?",
            "Any memorable events today?",
            "How would you rate your mood today? (On a scale of 1 to 10)",
            "Did you exercise today? If yes, what type of exercise did you do?",
            "What was the most challenging aspect of your day?",
            "Did you have any meaningful conversations today?",
            "How many hours of sleep did you get last night?",
            "What's one thing you would like to improve about your day?",
            "What are your top priorities for tomorrow?"
        ]
        # Select a random question
        question = random.choice(questions)
        return question
        '''''
        for question in questions:
            answer = self.voice_input()
            self.add_daily_question_answer(question, answer) **'''
    def train_model(self):
        text_classifier = self.nlp.pipe(
            (" ".join(event["text"] for event in self.data["events"])),
            disable=["tagger", "parser", "ner"]
        )
        self.model = make_pipeline(text_classifier, SVC(kernel="linear"))

        labels = [self.label_event(event) for event in self.data["events"]]

        self.model.fit(self.data["events"], labels)

    def label_event(self, event):
        if "work" in event["text"].lower():
            return "Work"
        elif "learn" in event["text"].lower():
            return "Learning"
        else:
            return "Personal"

    def search_and_save_data(self, query):

    # Code to search the internet for data related to the query and save it as CSV
        pass
    def bing_search(self, query):
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        subscription_key = "948b75c0956b46e5a3422ccc513e3c62"

        headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
        params  = {"q": query, "textDecorations": True, "textFormat": "HTML"}

        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        return search_results.get("webPages", {}).get("value", [])
    def start_listening(self):
        self.is_listening = True
        self.engine.say("I am listening")
        self.engine.runAndWait()
        while self.is_listening:
            user_input = self.voice_input()
            if not user_input:
                continue

            query_doc = self.spacy_model(user_input)
            max_similarity = -1
            max_intent = None

            for intent, examples in self.intents.items():
                for example in examples:
                    example_doc = self.spacy_model(example)
                    similarity = query_doc.similarity(example_doc)

                    if similarity > max_similarity:
                        max_similarity = similarity
                        max_intent = intent

            if max_intent == "add_event":
                self.add_event(user_input)
                self.save_to_file()
                self.engine.say("Event added successfully!")
                self.engine.runAndWait()

            elif max_intent == "add_relationship":
                self.add_relationship(user_input)
                self.save_to_file()
                self.engine.say("Relationship added!")
                self.engine.runAndWait()

            elif max_intent == "learn":
                subject = self.voice_input()
                self.add_learning_progress(subject, user_input)
                self.save_to_file()
                self.engine.say("Learning progress added!")
                self.engine.runAndWait()

            elif max_intent == "daily_questions":
                self.ask_daily_questions()
                self.save_to_file()
                self.engine.say("Daily questions answered and recorded!")
                self.engine.runAndWait()

            elif max_intent == "train_model":
                self.train_model()
                self.engine.say("Model trained!")
                self.engine.runAndWait()

            elif max_intent == "search":
                query = self.voice_input()
                results = self.bing_search(query)
                # Saving search results to a file - adjust saving method according to your needs
                with open("search_results.json", "w") as f:
                    json.dump(results, f)

                self.engine.say(f"Found {len(results)}  for your search!")
                self.engine.runAndWait()

            elif max_intent == "stop" or "shutdown the program":
                self.is_listening = False
                self.engine.say("Stopping listening mode")
                self.engine.runAndWait()

            elif max_intent == "ask_question":
                # Assuming `ask_daily_question` function returns a single question
                question = self.ask_daily_question()
                self.engine.say(question)
                self.engine.runAndWait()

                answer = self.voice_input()
                self.add_daily_question_answer(question, answer)
                self.engine.say("Your answer has been recorded!")
                self.engine.runAndWait()

            else:
                print("Sorry, I didn't understand that. Please provide a valid command.")


if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.start_listening()


