# Your Python code goes here
# Excercise 9 solution

# from os import system. for mac
# names=['john','sandeep']
# for name in names:
#     system(f"hello {name}")
import win32com.client

# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# List of names
names = ['john', 'sandy']

# Loop through each name and greet them
for name in names:
    speaker.Speak(f"Hello {name}")
