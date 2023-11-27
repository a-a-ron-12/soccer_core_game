
import time
import random
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


# Set the start time and duration
duration = 10
start_time = time.time()
color_list = ["blue", "green", "purple", "yellow"]

# Loop through as many times before the duration ends
while (time.time() - start_time) < duration:
    
    random.shuffle(color_list)
    
    text_to_voice(color_list[0])
    print(color_list[0])
    
text_to_voice("STOP! Game Over; you lose!")
