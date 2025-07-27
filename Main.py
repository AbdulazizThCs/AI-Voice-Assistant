from flask import Flask, render_template, request, jsonify
# Flask is used to create a simple web server to handle user interaction and backend processing

from STT import transcribe_audio, record_audio
from NLP import generate_reply
from TTS import speak

app = Flask(__name__)  # Create Flask web app instance

@app.route("/")
def home():
    # Serve the main page with the chat interface
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    # 1. Record audio from user microphone
    audio = record_audio()

    # 2. Convert recorded audio to text
    text = transcribe_audio(audio)

    # 3. Generate chatbot reply using NLP model
    reply = generate_reply(text)

    # 4. Convert reply text to speech and play it
    speak(reply)

    # Return JSON response with user's text and bot reply
    return jsonify({"user_text": text, "bot_reply": reply})

if __name__ == "__main__":
    # Run the Flask app in debug mode for development
    app.run(debug=True)