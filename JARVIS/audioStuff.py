import pyttsx3 as tts
import speech_recognition as sr
from datetime import datetime

def speak(statement, prnt=True):
    '''This function takes an argument in string format and then Computer speaks that string
    '''
    if prnt:
        print(statement)
    engine.say(statement)
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
    speak("I am Jarvis ! Please tell me how may I help you", False)

def takeCommand():
    '''
    This will record the sound from microphone and returns String query 
    '''

    # Self Added Awake Section -> Pending

    r = sr.Recognizer()
    r.pause_threshold = 1
    r.non_speaking_duration = .3
    r.energy_threshold = 200
    with sr.Microphone() as source :
        print("Listning...")
        audio = r.listen(source)

    try :
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_sphinx(audio, language='en-in') -> This is not working
        print(f"User Said : {query}\n")
        # There are many functions to recognise the audio but we are using that of google; Other are form IBM, AWS, Azure and many more
        # recognise_google only works online. The Only offline recogniser is sphinx which requires a module PocketSphinx

    except Exception as e :
        print(e)
        speak("Could not recognise. Please Say that again...")
        return "None"
    
    return query




# This is initialisation goes with must be done before execution 
engine = tts.init('sapi5')
voices = engine.getProperty('voices')

# To get the detail of the voices 
# print(voices[1].id)
# Setting up the Voices for the system
engine.setProperty('voice',voices[0])
