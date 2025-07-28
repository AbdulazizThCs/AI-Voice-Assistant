## AI-Voice-Assistant  
AI voice assistant that understands and responds instantly .

## Project Idea
An intelligent Arabic voice assistant that listens to user speech, generates contextual responses, and replies using realistic human-like voices—all within seconds. Built using a modular Python architecture, and deployed with a modern web interface. Developed after creating a Python environment using Anaconda.

## Features
- Fast response time: 4–5 seconds on average  
- Human-like speech output using ElevenLabs API  
- Smart Arabic understanding via Cohere NLP  
- Integrated with a sleek and interactive web interface  
- Modular and easy-to-extend file structure

## Project Structure
`Main.py # Core application logic  
 STT.py # Speech-to-text using Faster-Whisper  
 NLP.py # Text analysis and response generation using Cohere  
 TTS.py # Text-to-speech using ElevenLabs  
 templates/index.html # Web frontend (HTML)  
 static/style.css # Styling for the frontend (CSS)`  

## Used Libraries

- `faster_whisper` – for fast and accurate Arabic speech-to-text  

- `sounddevice` – to record real-time audio from the microphone  

- `numpy` – for numerical operations and array handling  

- `cohere` – for generating smart responses using NLP  

- `requests` – for sending API requests  

- `pygame` – to play audio output  

- `flask` – for running a lightweight web interface

## How to Run the Project

1. **Install [Anaconda](https://www.anaconda.com)**  
2. **Open Anaconda Terminal**  
3. **Create a virtual environment:** `conda create -n project_name python=3.10`
4. **Activate the environment:** `conda activate project_name`
5. **Installing Libraries:** `pip install faster-whisper sounddevice numpy cohere requests pygame flask`
6. **Open VSCode:** `code .`
7. Download the project files and run:

## Project Demo

https://github.com/user-attachments/assets/512739d3-1fbb-4b89-8a08-13461f9de480  

<hr>  

Developed by **Abdulaziz AL-Thomali**



