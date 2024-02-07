# views.py
from django.shortcuts import render

#def record_audio(request):
    # Add logic for recording audio
   # return render(request, 'audio_recording.html')


import os
import wave
import pyaudio

class AudioRecorder:
    def __init__(self):
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.recordings_folder = "recordings"
        os.makedirs(self.recordings_folder, exist_ok=True)

    def record_audio(self, duration=5, filename="default.wav"):
        """
        Record audio for a specified duration and save it to a WAV file.
        """
        p = pyaudio.PyAudio()

        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.sample_rate,
                        input=True,
                        frames_per_buffer=self.chunk)

        print(f"Recording audio for {duration} seconds...")

        frames = []
        for i in range(0, int(self.sample_rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        print("Recording complete.")

        stream.stop_stream()
        stream.close()
        p.terminate()

        self.save_audio(frames, filename)

    def save_audio(self, frames, filename):
        """
        Save audio frames to a WAV file.
        """
        wf = wave.open(os.path.join(self.recordings_folder, filename), 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(self.format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        print(f"Audio saved as {filename}.")

    def list_recordings(self):
        """
        List all available recordings in the recordings folder.
        """
        print("Available Recordings:")
        for filename in os.listdir(self.recordings_folder):
            print(filename)

    def play_recording(self, filename):
        """
        Play a specific recording.
        """
        p = pyaudio.PyAudio()

        wf = wave.open(os.path.join(self.recordings_folder, filename), 'rb')

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        print(f"Playing {filename}...")

        data = wf.readframes(self.chunk)

        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)

        print("Playback complete.")

        stream.stop_stream()
        stream.close()
        p.terminate()


# Integrate the AudioRecorder into the Jarvis app
class Jarvis:
    def __init__(self):
        self.audio_recorder = AudioRecorder()

    def run(self):
        # Your existing code for the personal assistant app

        # Example use cases for the audio recorder
        self.audio_recorder.record_audio(duration=10, filename="lecture.wav")
        self.audio_recorder.list_recordings()
        self.audio_recorder.play_recording("lecture.wav")


# Instantiate and run the PersonalAssistant
if __name__ == "__main__":
    assistant = Jarvis()
    assistant.run()
