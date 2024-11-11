import pyttsx3
import time

"""
Author: Nitesh Kumar
Date: Single's Day, 11th November 2024
Version: 0.4

Explored pyttsx3 (Python Text-to-Speech version 3) and win32com (Windows COM API) 
with all other test files in the repositories.

This script gives shoutouts to a list of names using the pyttsx3 text-to-speech engine.
"""

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get the available voices and select the first one
voices = engine.getProperty("voices")

# List of names to give a shoutout to
names = ["Nitesh", "Shivam", "Hari Ohm", "Koushal", "Kushi", "Soumya", "Rakhsa", "Diksha"]

# Customizing voice settings (optional)
engine.setProperty('voice', voices[0].id)  # Set voice to the first available one
engine.setProperty('rate', 170)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume (range from 0.0 to 1.0)

# Loop through each name and give a shoutout
for name in names:
    shoutout_text = f"Shoutout to {name}!"  # Create shoutout text
    print(shoutout_text)  # Optional: Print the shoutout to the console
    engine.say(shoutout_text)  # Make the engine speak the shoutout
    engine.runAndWait()  # Wait for the speech to finish before continuing

    # Optional: Small delay between shoutouts to ensure smooth output
    time.sleep(0.5)

# Comments added by ChatGPT
