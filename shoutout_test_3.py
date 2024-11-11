import pyttsx3

"""
Author: Nitesh Kumar
Date: Single's Day, 11th November 2024
Version: 0.3

Explored pyttsx3 (Python Text-to-Speech version 3) for text-to-speech functionality.
This script demonstrates how to initialize pyttsx3, select a voice, and use it to speak text.
"""

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Choose a voice (you can loop through or select a specific index)
# Example: Selecting the first voice
# 0 for male and 1 for female (commonly available voices)
engine.setProperty('voice', voices[1].id)  # Select the female voice (index 1)

# Set speech rate (optional)
engine.setProperty('rate', 150)  # Adjust the speed as needed (higher for faster, lower for slower)

# Set volume (optional)
engine.setProperty('volume', 0.9)  # Volume level between 0.0 and 1.0 (1.0 being maximum)

# Input text to be spoken
text = "Hello! This is a SAPI5 text-to-speech example using Python."

# Speak the text
engine.say(text)

# Wait for the speaking to finish
engine.runAndWait()  # This ensures the program waits until speech is finished

# Comments added by ChatGPT
