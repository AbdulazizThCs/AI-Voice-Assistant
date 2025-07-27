import requests
import pygame
from io import BytesIO

API_KEY = "sk_171f83fcf68f5a322a10a494061642fc4d0b4cfd6e0254cc"
VOICE_ID = "rPNcQ53R703tTmtue1AT"

def speak(text):
    # Convert text to speech and play audio immediately
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    # Send POST request to ElevenLabs API
    resp = requests.post(url, json=payload, headers=headers, stream=True)
    resp.raise_for_status()  # Raise error if request failed

    # Initialize pygame mixer and load audio from memory
    pygame.mixer.init()
    audio_stream = BytesIO(resp.content)
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    # Wait until audio playback is finished
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Quit the mixer to free resources
    pygame.mixer.quit()