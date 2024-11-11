import win32com.client

"""
Author: Nitesh Kumar
Date: Single's Day, 11th November 2024
Version: 0.2

Explored pyttsx3 (Python Text-to-Speech version 3) and win32com (Windows COM API) 
with all other test files in the repositories.

This script uses the win32com.client library to interact with the Microsoft Speech API 
(SAPI) to provide text-to-speech functionality. It iterates through a list of names and 
speaks out a custom message for each.
"""

# Create an instance of the SAPI SpVoice object for text-to-speech functionality
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# List of names to give shoutouts to
names = ["Nitesh", "Shivam", "Hari Ohm", "Koushal", "Kushi", "Soumya", "Rakhsa", "Diksha"]

# Iterate through each name and generate a shoutout message
for name in names:
    shoutout_text = f"My self {name}, I am a BCA student"  # Create shoutout text for each name
    print(shoutout_text)  # Print the shoutout message (optional)
    speaker.Speak(shoutout_text)  # Use the speaker object to speak the shoutout aloud

# Comments added by ChatGPT
