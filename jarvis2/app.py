import spacy
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pyttsx3
import datetime
import requests
import csv


class PersonalAssistant:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.data = {"events": [], "relationships": [], "learning": [], "daily_questions": []}
        self.model = None
        self.engine = pyttsx3.init()
        self.is_listening = False

    def voice_input(self):
    # Code to record audio and convert it to text
        pass

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

    def ask_daily_questions(self):
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

        for question in questions:
            answer = self.voice_input()
            self.add_daily_question_answer(question, answer)

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


    def start_listening(self):
        self.is_listening = True
        self.engine.say("Starting listening mode")
        self.engine.runAndWait()
        while self.is_listening:
            user_input = self.voice_input()
            if not user_input:
                continue

            if "event" in user_input.lower():
                self.add_event(user_input)
                print("Event added!")
            elif "relationship" in user_input.lower():
                self.add_relationship(user_input)
                print("Relationship added!")
            elif "learn" in user_input.lower():
                subject = input("Enter the subject of learning: ")
                self.add_learning_progress(subject, user_input)
                print("Learning progress added!")
            elif "daily questions" in user_input.lower():
                self.ask_daily_questions()
                print("Daily questions answered and recorded!")
            elif "train model" in user_input.lower():
                self.train_model()
                print("Model trained!")
            elif "search" in user_input.lower():
                query = input("Enter a query: ")
                self.search_and_save_data(query)
                print("Search results saved!")
            elif "stop listening" in user_input.lower():
                self.is_listening = False
                self.engine.say("Stopping listening mode")
                self.engine.runAndWait()
                print("Listening mode stopped!")
            else:
                print("Sorry, I didn't understand that. Please provide a valid command.")


if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.start_listening()


