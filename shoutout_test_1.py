import pyttsx3

"""
Author: Nitesh Kumar
Date: Single's Day, 11th November 2024
Version: 0.1

Explored pyttsx3 (Python Text-to-Speech version 3) for text-to-speech functionality.
This script demonstrates how to initialize pyttsx3, set voice properties, and use it 
to give a shoutout message.
"""

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Get the list of available voices
voices = speaker.getProperty('voices')

# Set the desired voice (0 for the first voice, 1 for the second, etc.)
speaker.setProperty('voice', voices[0].id)  # Change the index if needed

# Set speech rate (optional)
speaker.setProperty('rate', 150)  # Adjust the speech rate (words per minute)

# Set volume (optional)
speaker.setProperty('volume', 1.0)  # Volume between 0.0 and 1.0

# Name for the shoutout
name = "BATMAN"

# Create the shoutout message
shoutout = f"This is {name}"  # Create the message with the name
print(shoutout)  # Print the message (optional)

# Speak the message
speaker.say(shoutout)  # Speak the shoutout aloud
speaker.runAndWait()  # Wait for the speech to finish before continuing

# Comments added by ChatGPT
