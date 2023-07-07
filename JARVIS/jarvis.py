import pyttsx3 as tts
from datetime import datetime
import speech_recognition as sr


'''
pyttsx3 -> Test to Speech
datetime -> To get the current time

'''

engine = tts.init('sapi5')
voices = engine.getProperty('voices')

# To get the detail of the voices 
# print(voices[1].id)

# Setting up the Voices for the system
engine.setProperty('voice',voices[0])



def speak(audio):
    '''This function takes an argument in string format and then Computer speaks that string
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''This Function will make your Jarvis wish you according to system time. And tell the system time also
    '''
    hour = datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir !")
    elif hour >= 12 and hour < 17 :
        speak("Good AfterNoon Sir !")
    else :
        speak("Good Evening Sir !")
    
    curTime = datetime.now().strftime("%H:%M")
    speak(f"Current time is {curTime}")
    speak("I am Jarvis ! Please tell me how may I help you")

if __name__ == '__main__':
    # speak("Ayush is Awesome")
    wishMe()
