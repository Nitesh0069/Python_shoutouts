import win32com.client

"""
Author: Nitesh Kumar
Date: Single's Day, 11th November 2024
Version: 0.5

Explored pyttsx3 (Python Text-to-Speech version 3) and win32com (Windows COM API) 
with all other test files in the repositories.

This script demonstrates the usage of the win32com.client library to interact with 
the Microsoft Speech API (SAPI) for text-to-speech functionality.
"""

# Create an instance of the SAPI SpVoice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Get the available voices
voices = speaker.GetVoices()

# List available voices and their IDs (for reference)
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.GetDescription()}")  # Prints the description of each voice

# Set a specific voice by index (e.g., voice 0 or 1)
# Here, we select the first voice (0th index)
speaker.Voice = voices.Item(0)  # Change the index for different voices

# Now, use the voice to speak
speaker.Speak(f"Hello, I am using the first available voice.")  # Speaks the text out loud

# Comments added by ChatGPT
