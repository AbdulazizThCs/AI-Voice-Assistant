import os
# Temporary fix for OpenMP conflict
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np

DURATION = 5  # seconds
SAMPLE_RATE = 16000  # Hz

# Load Whisper model once
model = WhisperModel("medium", compute_type="int8")

def record_audio():
    # Record audio from microphone
    print("Recording...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    print("✅ Done")
    return audio

def transcribe_audio(audio):
    # Convert audio to text using Whisper model
    audio = audio.flatten().astype(np.float32) / 32768.0  # normalize audio
    segments, _ = model.transcribe(audio, language="ar", beam_size=1)
    text = "".join([seg.text for seg in segments])
    return text