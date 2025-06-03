# The Interactive Bot Orator

This is a small weekend project that demonstrates how to pipeline various local open source AI technologies to build a speech-to-speech AI bot. The goal is to create a fully local assistant that listens to your speech, transcribes it, generates a response using a local language model, and speaks the response back to you—all without relying on cloud services.

## Features
- **Speech Recognition:** Uses Vosk for offline speech-to-text.
- **Conversational AI:** Integrates with Ollama to run a local LLM for generating responses.
- **Text-to-Speech:** Uses pyttsx3 for offline speech synthesis.
- **Audio Input/Output:** Utilizes sounddevice for capturing and playing audio.

## How It Works
1. The bot listens to your voice through your microphone.
2. Vosk transcribes your speech to text.
3. The transcribed text is sent to a local LLM (via Ollama) to generate a response.
4. The response is spoken back to you using pyttsx3.

## Requirements
- Python 3.8+
- [Vosk](https://alphacephei.com/vosk/)
- [Ollama](https://ollama.com/) (running a local model)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [sounddevice](https://pypi.org/project/sounddevice/)

Install dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Download and set up a Vosk model in the `Model/` directory.
2. Make sure Ollama is running and accessible at `http://localhost:11434`.
3. Run the bot:
```
python main.py
```
4. Speak into your microphone. The bot will listen, respond, and speak back.

## Notes
- All processing is done locally; no data is sent to the cloud.
- This project is for educational and experimental purposes.

## License
See the `LICENSE` file for details. Third-party licenses are listed in `NOTICE`.
