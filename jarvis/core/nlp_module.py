from transformers import pipeline

# Initialize the NLP pipeline
nlp_pipeline = pipeline("ner")

# Perform natural language processing
def analyze_text(text):
    result = nlp_pipeline(text)
    return result

# Example usage
user_input = "Set a reminder for tomorrow at 3 PM."
analysis_result = analyze_text(user_input)
print("NLP Analysis:", analysis_result)
