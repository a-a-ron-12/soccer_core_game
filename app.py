
# Import libraries
import time
import random
import pyttsx3

from voice_function import text_to_voice

# Define main variables
color_list = ["green", "blue", "yellow", "red"]
duration = 60
start_time = time.time()

# Start Level One
text_to_voice("Level 1 is about to begin.")

# Loop until duration limit is met
while (time.time() - start_time) < duration:

    # Shuffle list
    random.shuffle(color_list)
    print(color_list[0])
    
    # Conver to speech
    text_to_voice(color_list[0])

# End Game
stop_message = "STOP! Game Over; you lose!"
text_to_voice(stop_message)