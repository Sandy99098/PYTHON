# Your Python code goes here
#  excercise 9
#  write a program to pronounce the lsit of names using win32 APi.
#  if yoy are given a list of 

 
import win32com.client

# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Function to convert text to speech
def speak(text):
    speaker.Speak(text)

# Example usage
if __name__ == "__main__":
    l=['Jay ','Hari','Geeta','bishnu']

for i in range (len(l)):
    speak(f"Hello {l[i]} . k chha ")
 
 
    # speak(l)
