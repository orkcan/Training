# views.py
from django.shortcuts import render

def record_audio(request):
    # Add logic for recording audio
    return render(request, 'audio_recording.html')
