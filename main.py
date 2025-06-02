import vosk
import sounddevice as sd
import json
from ollama import Client
import pyttsx3
import re


print("Loading voice ...")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 215)

# Load Vosk model (download a model and set the path if needed)
print("Loading Vosk ...")
# Careful, you must give the path to your model
model = vosk.Model("Model")
rec = vosk.KaldiRecognizer(model, 16000)

#load ollama model
print("Loading model ...")
messages = [{'role':'system', 'content':'Only use normal characters. No asterisks'}]
client = Client(host='http://localhost:11434')

# Function to listen and recognize speech
print("Say something!")

def listen_and_respond():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1) as stream:
        print("Listening...")

        while True:
            data, _ = stream.read(4000)
            data_bytes = bytes(data)

            if rec.AcceptWaveform(data_bytes):
                result = rec.Result()
                text = json.loads(result)["text"]
                if text:
                    # Remove all characters except letters, spaces, periods, and commas
                    print(f"You said: {text}")
                    messages.append({'role': 'user', 'content': text})

                    response = client.chat(
                        model='gemma3:4b',
                        messages=messages
                    )
                    reply = response['message']['content']
                    messages.append({'role': 'assistant', 'content': reply})
                    print(f"Assistant: {reply}")
                    engine.say(reply)
                    engine.runAndWait()

                    if "exit" in text or "quit" in text:
                        print("Exiting...")
                        break
listen_and_respond()