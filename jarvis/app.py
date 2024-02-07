# Import the necessary libraries
import speech_recognition as sr
import spacy
from spacy.util import minibatch, compounding
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from joblib import dump, load
from sklearn.metrics import accuracy_score

def voice_input():
    """
    The purpose of this function is to record audio and convert to text using Google's voice recognition API.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {str(e)}")
    return None

def load_data():
    """
    This function attempts to load the IMDB movie reviews corpus from sklearn and return sentences and labels as a tuple.
    """
    try:
        movie_reviews_data = load_files(r"jarvis/imdb_data/test", shuffle=True)
        sentences = movie_reviews_data.data
        labels = movie_reviews_data.target
        return sentences, labels
    except Exception as e:
        print("Failed to load the data.")
        print(f"Error: {e}")
        return None, None

# The rest of your existing functions ...

if __name__ == "__main__":
    sentences, labels = load_data()
    if not sentences or not labels:
        print("Error loading data.")
    else:
        sentences_train, sentences_test, labels_train, labels_test = train_test_split(sentences, labels, test_size=0.2, random_state=42)
        model = train_model(sentences_train, labels_train)
        if not model:
            print("Error in model training.")
        else:
            evaluate_model(model, sentences_test, labels_test)
            loaded_model = load_model()
            if not loaded_model:
                print("Error in loading model.")
            else:
                interactive_console(loaded_model)