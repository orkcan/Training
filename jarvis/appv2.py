import spacy
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
import pyttsx3
import datetime

class PersonalAssistant:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.data = {"events": [], "relationships": [], "learning": [], "daily_questions": []}
        self.model = None
        self.engine = pyttsx3.init()

    def voice_input(self):
        """
        Record audio and convert it to text using the speech_recognition library.
        """
        # Similar to your existing voice_input function

    def add_event(self, event_text):
        """
        Add an event to the data.
        """
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["events"].append({"text": event_text, "date": date})

    def add_relationship(self, relationship_text):
        """
        Add a relationship to the data.
        """
        self.data["relationships"].append({"text": relationship_text})

    def add_learning_progress(self, subject, progress_text):
        """
        Add learning progress to the data.
        """
        self.data["learning"].append({"subject": subject, "text": progress_text})

    def add_daily_question_answer(self, question, answer):
        """
        Add a daily question and answer to the data.
        """
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.data["daily_questions"].append({"question": question, "answer": answer, "date": date})

    def ask_daily_questions(self):
        """
        Ask a set of daily questions to cover various aspects of a person's life.
        """
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
        """
        Train a text classification model using spaCy and linear SVM.
        """
        text_classifier = self.nlp.pipe(
            (" ".join(event["text"] for event in self.data["events"])),
            disable=["tagger", "parser", "ner"]
        )
        self.model = make_pipeline(text_classifier, SVC(kernel="linear"))

        # Assuming labels for events are generated based on the date or context
        labels = [self.label_event(event) for event in self.data["events"]]

        self.model.fit(self.data["events"], labels)

    def label_event(self, event):
        """
        Dummy function to generate labels for events. Modify as needed.
        """
        # Example: classify events as "Work", "Personal", or "Learning"
        if "work" in event["text"].lower():
            return "Work"
        elif "learn" in event["text"].lower():
            return "Learning"
        else:
            return "Personal"

    def interactive_console(self):
        """
        An interactive console to get user input and interact with the assistant.
        """
        while True:
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
            elif "exit" in user_input.lower():
                break
            else:
                print("Sorry, I didn't understand that. Please provide a valid command.")

if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.interactive_console()

"""
In this updated code, I added a new function ask_daily_questions that asks daily questions and registers the answers. 
The questions are predefined, but you can customize them according to your needs. 
The add_daily_question_answer function is used to store the answers along with the corresponding question and date.

Remember to customize and extend these functions based on your specific requirements and use case.
"""
