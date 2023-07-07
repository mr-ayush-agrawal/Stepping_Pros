import wikipedia as wiki
import webbrowser as web
from audioStuff import *

'''
pyttsx3 -> Test to Speech
datetime -> To get the current time
speech_recognition -> To take the audio input
wikipedia -> To search through wikipedia
webbrowser -> open any link
'''

def openSomething(query):
    if 'brave' in query:
        pass
    elif 'youtube' in query :
        speak("Opening Youtube in a new window", False)
        web.open_new("youtube.com")
    elif 'google' in query :
        speak("Opening Google in a new window", False)
        web.open_new("google.com")


if __name__ == '__main__':
    wishMe()
    # while True :
    if True :
        query = takeCommand().lower()

        # Logic to implementing the tesks
        if 'open' in query:
            openSomething(query)

        elif 'search' in query :
            # searchSomething(query) -> To be defined same as openSomething ->Pending
            pass
        
        elif 'wikipedia' in query:
            query.replace('wikipedia' , "")
            speak("Searching Wikipedia...\n")
            result = wiki.summary(query, sentences = 2)
            speak("According to wikipedia ...")
            speak(result)

        elif 'exit' in query :
            speak("Exiting the program...", False)
            exit()