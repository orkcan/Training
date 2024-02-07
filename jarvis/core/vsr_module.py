from transformers import pipeline

# Initialize the ASR pipeline
asr_pipeline = pipeline("automatic-speech-recognition")

# Perform speech recognition
def recognize_speech(audio_file_path):
    result = asr_pipeline(audio_file_path)
    return result

# Example usage
audio_file_path = "path/to/your/audio/file.wav"
transcription = recognize_speech(audio_file_path)
print("Transcription:", transcription)