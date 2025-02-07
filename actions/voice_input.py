# actions/voice_input.py
from typing import Any, Text, Dict, List
from aiogram import Dispatcher
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave
import os
from google.cloud import speech_v1
from google.cloud.speech_v1 import types

class ActionVoiceInput(Action):
    def name(self) -> Text:
        return "action_voice_input"

    def record_audio(self, duration=5, sample_rate=16000):
        """Record audio from microphone"""
        Dispatcher.utter_message(text="Starting to record... Please speak.")
        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype='int16'
        )
        sd.wait()  # Wait until recording is finished
        return recording, sample_rate

    def save_audio(self, recording, sample_rate, filename='input.wav'):
        """Save the recording as a WAV file"""
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(sample_rate)
            wf.writeframes(recording.tobytes())
        return filename

    def transcribe_google_cloud(self, audio_file):
        """Transcribe audio using Google Cloud Speech-to-Text"""
        client = speech_v1.SpeechClient()

        with open(audio_file, 'rb') as audio_file:
            content = audio_file.read()

        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(
            encoding=types.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='en-US',
            model='command_and_search',
            enable_automatic_punctuation=True
        )

        response = client.recognize(config=config, audio=audio)
        
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "
            
        return transcript.strip()

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # Record audio
            dispatcher.utter_message(text="Starting voice recording...")
            recording, sample_rate = self.record_audio()
            
            # Save audio to file
            audio_file = self.save_audio(recording, sample_rate)
            
            # Transcribe audio
            transcript = self.transcribe_google_cloud(audio_file)
            
            if transcript:
                dispatcher.utter_message(text=f"I heard: {transcript}")
                # Clean up the audio file
                os.remove(audio_file)
                
                # Return the transcribed text for further processing
                return [{"event": "user", "text": transcript}]
            else:
                dispatcher.utter_message(text="I couldn't understand what you said. Please try again.")
                
        except Exception as e:
            dispatcher.utter_message(text=f"Error processing voice input: {str(e)}")
        
        return []