
# Import libraries
import time
import random
import pyttsx3

from voice_function import text_to_voice

# Define main variables
# Currently 3 levels designed
level = 1
duration = 60
stop_message = "STOP! This round is over."

# Establish colors to be called
color_list = ["green", "blue", "yellow", "red"]
fake_color_list = ["pink", "purple", "orange", "black", "white"]
random.shuffle(color_list)
previous_color = color_list[0]

start_time = time.time()

# Start Level One
text_to_voice(f"Level {level} is about to begin.")
time.sleep(1)

# Loop until duration limit is met
while (time.time() - start_time) < duration:
# Run this loop everytime until the current time has reached 60 seconds

    # Add a fake color to the color list
    if level == 1:
        
        # Create a copy of the color list
        temp_color_list = color_list.copy()
        
        # Shuffle fake color list and add fake color
        random.shuffle(fake_color_list)
        fake_color = fake_color_list[0]
        temp_color_list.append(fake_color)
        
        # Shuffle new color list and choose first color
        random.shuffle(temp_color_list)
        color = temp_color_list[0]
        
        # Do not repeat the previous color
        if color == previous_color:
            color = temp_color_list[1]
            
        previous_color = color

        
    # No repetitive colors back to back
    elif level == 2:
        
        # Shuffle color list and choose color
        random.shuffle(color_list)
        color = color_list[0]
        
        # Do not repeat the previous color
        if color == previous_color:
            color = color_list[1]
            
        previous_color = color

        
    # Call two levels at the same time   
    elif level == 3:
        
        random.shuffle(color_list)
        double_color_list = color_list[:2]
        color = " ".join(double_color_list)

    
    # Convert to speech
    text_to_voice(color)
    
    # Add a time delay to this level
    if level == 3:
        time.sleep(1)

# End Game
text_to_voice(stop_message)