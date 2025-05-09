import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment
import io
import os

class BiharVoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.voices = {
            'hi': 'indian',
            'en': 'english',
            'ur': 'urdu'
        }
        
    def text_to_speech(self, text, language='en'):
        try:
            # Set voice properties based on language
            voices = self.engine.getProperty('voices')
            if language in self.voices:
                for voice in voices:
                    if self.voices[language] in voice.name.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
            
            self.engine.say(text)
            self.engine.runAndWait()
            return True
        except Exception as e:
            print(f"TTS Error: {e}")
            return False
            
    def speech_to_text(self, language='en'):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""