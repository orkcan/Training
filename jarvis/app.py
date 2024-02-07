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
        movie_reviews_data = load_files(r"imdb_data/test/pos/", shuffle=True)
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



"""""  
Together, these functions train a text classification model using the movie review sentences and 
corresponding sentiment labels. The trained model is then saved to disk so that 
it can be reused without needing to train it again. The saved model can be loaded from disk 
and evaluated on a test dataset to determine its accuracy (the percentage of correct predictions). 
The interactive console allows a user to interact with the classifier by speaking into the microphone. 
The user('s spoken language is converted into text, which the model then uses to predict the sentiment. '
'The model')s prediction is printed out to the console.



Choose a server: Many cloud providers such as Google Cloud, Amazon Web Services (AWS), Microsoft Azure, and Heroku offer cloud servers where you can deploy your code. Some even have free tiers where you can run small applications without any charges.
Set Up the Server: Once you've chosen a server, you need to set it up. This involves installing Python, and any other dependencies you might need to run your code (like SpeechRecognition, spacy, sklearn etc). Each cloud provider has instructions on how to do this.
Upload Your Code: After your server is set up, you can upload your Python script. You can do this through an SSH client (like Putty or Terminal if you're on a Mac) or through any other upload method that the cloud provider offers.
Train the Model: Now you should be able to run your python script on the server. You can use the command python scriptname.py in the terminal to run the script. However, do note that training the model on a typically-sized dataset would require quite a bit of time and resources. If your server is not powerful enough, this might not be possible.
Deploy the Model: After the model is trained, you can save the model using joblib (joblib.dump in your script). Now you can use this trained model file in any app, website, or API.
Serve Your Model: Now that you have a trained model, you want to use it to make predictions in production. For this, you can build a web application (using Flask/Django for Python) or an API (Flask-RESTful or Django REST framework). Then your application or API can be called from your frontend.
Now, regarding developing this application, you would need an integrated development environment (IDEs) to write and manage your codes. You can try PyCharm, Jupyter Notebook or Visual Studio Code.
In addition, here are some things to consider:
Learning basics of Python: If you have zero experience in software development, I highly recommend learning basic Python syntax first. There are many free resources like Codecademy and Coursera that could be helpful.
Libraries: Learn how to use the libraries that you've included in your script, like Scikit-learn, spaCy, etc. This will help you understand how the code is functioning.
Setting up locally: Try running your code on your own machine first. Install Python and the required libraries and run your script. If any errors occur, it's much easier to debug on your own machine.
Git: Learn how to use Git. Git is a version control system that helps you track your code and collaborate with others. Many servers and cloud-based services integrate with Git, making deployment seamless.

"""""