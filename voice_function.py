
import pyttsx3


def text_to_voice(text):
    
    # Initialize the TTS engine
    tts_engine = pyttsx3.init()

    # Set the voice for Spanish (assuming you have a Spanish voice pack installed)
    voices = tts_engine.getProperty('voices')
    
    tts_engine.setProperty('voice', voices[1].id)  # Sabina Mexico Spanish voice (2)
    tts_engine.setProperty('rate', 100)   # Default is 150; slowed down for better understanding

    # Convert text to speech
    tts_engine.say(text)

    # Play the speech
    tts_engine.runAndWait()