import wikipedia as wiki
import webbrowser as web
import os
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
    elif 'stack overflow'  in query :
        speak("Opening Stackoverflow in a new window", False)
        web.open_new("stackoverflow.com")
    elif 'mail' in query :
        speak("Opening Mail Inbox in a new window", False)
        web.open_new("https://mail.google.com/mail/u/0/#inbox")
    elif 'email' in query :
        speak("Opening Mail Inbox in a new window", False)
        web.open_new("https://mail.google.com/mail/u/0/#inbox")

    # Now opening Applications
    elif 'code' in query :
        codePath = r"C:\Users\Ayush\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        speak("Opening VS Code ", False)
        os.startfile(codePath)



if __name__ == '__main__':
    web.register('chrome', None)

    wishMe()
    while True :
    # if True :
        query = takeCommand().lower()

        # Logic to implementing the tesks
        if 'open' in query:
            openSomething(query)

        elif 'search' in query :
            # searchSomething(query) -> To be defined same as openSomething ->Pending
            pass
        
        elif 'wikipedia' in query:
            try :
                query.replace('wikipedia' , "")
                speak("Searching Wikipedia...\n")
                result = wiki.summary(query, sentences = 2)
                speak("According to wikipedia ...")
                speak(result)
            except :
                speak("Something went wrong... Please Try Again")

        elif 'exit' in query :
            speak("Exiting the program...", False)
            exit()

        # Email Portion I am not making.    -> May be later in future