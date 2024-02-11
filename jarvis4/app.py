import os
import requests
import datetime
from pydantic import BaseModel
from pandas import DataFrame
from sklearn import preprocessing
from sentence_transformers import SentenceTransformer
import speech_recognition as sr
import wikipedia
from wolframalpha import Client
import random
import pyttsx3


class Data(BaseModel):
    events: list
    relationships: list
    learning: list
    daily_questions: list

class States:
    LISTENING = "LISTENING"
    ADD_EVENT = "ADD_EVENT"
    ADD_RELATIONSHIP = "ADD_RELATIONSHIP"
    ADD_LEARNING = "ADD_LEARNING"
    ASK_QUESTION = "ASK_QUESTION"

class Jarvis:
    def __init__(self, data_filepath='data.parquet'):
        self.engine = pyttsx3.init()  # Initialize Text-to-Speech engine
        self.data = Data(events=[], relationships=[], learning=[], daily_questions=[])
        self.bing_search_url = "https://api.bing.microsoft.com/v7.0/search"
        self.headers = {"Ocp-Apim-Subscription-Key": os.getenv('948b75c0956b46e5a3422ccc513e3c62')}
        self.voice_recognizer = sr.Recognizer()  # Initialize speech recognition
        self.is_listening = True  # Control whether the assistant is actively listening
        self.filepath = data_filepath  # Save content to Parquet file
        self.weather_api_key = os.getenv('OPEN_WEATHER_API_KEY')  # Initialize OpenWeather client
        self.sent_transformer = SentenceTransformer('all-MiniLM-L6-v2')
        self.wolf_client = Client(os.environ.get('WOLFRAM_ALPHA_APP_ID'))  # Initialize Wolfram Alpha client
        self.create_parquet_file()  # Create Parquet file on init
        #self.check_api_keys()
        self.engine = pyttsx3.init()  # Initialize Text-to-Speech engine

    #def check_api_keys(self):
    #    if not (self.headers["Ocp-Apim-Subscription-Key"] and self.weather_api_key and self.wolf_client):
    #        raise ValueError("Some API keys are missing. Check your environment variables.")
    def text_to_speech(self, text):
        """Converts the incoming text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def change_state(self, command):
        if "add event" in command:
            return States.ADD_EVENT
        elif "add relationship" in command:
            return States.ADD_RELATIONSHIP
        elif "add learning" in command:
            return States.ADD_LEARNING
        elif "ask question" in command:
            return States.ASK_QUESTION

        return States.LISTENING
    def set_speech_engine_properties(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Changing index changes voices. Default voice is the first one.
        rate = self.engine.getProperty('rate')  # Speed percent (can go over 100)
        self.engine.setProperty('rate', 125)  # Speed percent (can go over 100)
        volume = self.engine.getProperty('volume')  # Volume 0-1
        self.engine.setProperty('volume', 1)  # Volume 0-1

    def create_parquet_file(self):
        df = DataFrame(self.data.dict())
        df.to_parquet(self.filepath)

    def update_parquet_file(self):
        df = DataFrame(self.data.dict())
        df.to_parquet(self.filepath, mode='overwrite')  # overwrite the existing content

    def voice_input(self):
        # before listening, say something to the user
        self.text_to_speech("I am listening master , please tell me your command")
        with sr.Microphone() as source:
            print("Listening master")
            self.voice_recognizer.pause_threshold = 1
            audio = self.voice_recognizer.listen(source)
        try:
            print("Recognizing...")
            query = self.voice_recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query

        except Exception as e:
            print(e)
            response = "I'm sorry, I was unable to recognize your voice."
            print(response)
            self.text_to_speech(response)
            return ""

    def add_event(self, event_text):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data.events.append({"text": event_text, "date": date})
        self.update_parquet_file()  # Update Parquet file after adding a new event

    def add_relationship(self, relationship_text):
        self.data.relationships.append({"text": relationship_text})
        self.update_parquet_file()  # Update Parquet file after adding a new relationship

    def add_learning_progress(self, subject, progress_text):
        self.data.learning.append({"subject": subject, "text": progress_text})
        self.update_parquet_file()  # Update Parquet file after adding a new learning progress

    def add_daily_question_answer(self, question, answer):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.data.daily_questions.append({"question": question, "answer": answer, "date": date})
        self.update_parquet_file()  # Update Parquet file after adding a new daily question answer

    def fetch_bing_search_results(self, query):
        try:
            response = requests.get(self.bing_search_url, headers=self.headers, params={'q': query})
            response.raise_for_status()
            search_results = response.json()
            for result in search_results.get('webPages', {}).get('value', []):
                name = result['name']
                url = result['url']
                self.data.events.append({
                    'name': name,
                    'url': url
                })
            self.update_parquet_file()  # Update Parquet file after fetching new data
        except requests.exceptions.RequestException as err:
            print(f"A request error occurred: {err}")

    def fetch_wikipedia_search_results(self, query, sentences=10):
        wikipedia_results = wikipedia.summary(query, sentences=sentences)
        self.text_to_speech(f"The result from Wikipedia is: {wikipedia_results}")

    def fetch_wolframalpha_answer(self, query):
        res = self.wolf_client.query(query)
        wolfram_alpha_answers = next(res.results).text
        return wolfram_alpha_answers

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
            "What are your top priorities for tomorrow?",
            "How can I assist you more efficiently?",
        ]
        # Select a random question
        question = random.choice(questions)
        # It's better to store the answer and ask the assistant to speak out the question
        # but for simplicity, let's return the question text for now
        return question
    def main_loop(self):
        self.state = States.LISTENING
        while True:
            try:
                if self.state == States.LISTENING:
                    command = self.voice_input().lower()
                    # voice input may return empty string
                    if command:
                        self.state = self.change_state(command)
                elif self.state == States.ADD_EVENT:
                    self.text_to_speech('What is the event details, master?')
                    command = self.voice_input().lower()
                    self.add_event(command)
                    self.text_to_speech('Event added successfully.')
                    self.state = States.LISTENING
                elif self.state == States.ADD_RELATIONSHIP:
                    self.text_to_speech('Can you tell me more about the relationship, master?')
                    command = self.voice_input().lower()
                    self.add_relationship(command)
                    self.text_to_speech('Relationship information was noted, master.')
                    self.state = States.LISTENING
                elif self.state == States.ADD_LEARNING:
                    self.text_to_speech('Can you tell me more about the learning progress, master?')
                    command = self.voice_input().lower()
                    self.add_learning_progress("auto-gen-prog", command)
                    self.text_to_speech('Noted your progress, master.')
                    self.state = States.LISTENING
                elif self.state == States.ASK_QUESTION:
                    self.text_to_speech('What is your question today, master?')
                    question = self.voice_input().lower()
                    self.text_to_speech('And your answer, master?')
                    answer = self.voice_input().lower()
                    self.add_daily_question_answer(question, answer)
                    self.text_to_speech('I have updated your daily question and answer, master.')
                    self.state = States.LISTENING
                elif 'exit' in command:  # say 'exit' to stop the program
                    self.text_to_speech('Goodbye, master.')
                    break
                else:
                    self.text_to_speech("Sorry, I didn't understand. Can you repeat please?")
                    self.state = States.LISTENING  # revert back to listening state

            except Exception as e:
                print(f"An error occured :{str(e)}")
                self.text_to_speech("An exception error occured. Resetting by putting the state in Listening")
                self.state = States.LISTENING
    def fetch_weather_information(self, city):
        try:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather',
                                    params={'q': city, 'appid': self.weather_api_key, 'units': 'metric'})
            response.raise_for_status()
            weather_data = response.json()
            self.data.events.append({
                "city": city,
                "description": weather_data["weather"][0]["description"],
                "temperature": weather_data["main"]["temp"]
            })
            self.update_parquet_file()  # Update Parquet file
        except requests.exceptions.RequestException as err:
            print(f"A request error occurred: {err}")

if __name__ == '__main__':
    jarvis = Jarvis()
    jarvis.main_loop()