'''
This Program Would Read the data form the newsapi.org
And Speak all the news headlines for

We can use differnt libraries for speaking -> Win32.clint.dispatch , ptttsx3 ....
There is a library of NewsApi also that can be used for this purpose but I will make the program
'''

import requests                         # For getting stuff form Internet
from win32com.client import Dispatch    # Using Speak
import json                             # Unpacking the stuffs

# Creating Speak Function that will speak the String
def speak(str):
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# API_KEY = input("Enter the API KEY of newsapi website\n")
API_KEY = 'YOUR API KEY HERE '

try :
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"   
except :
    print("Enter a valid API Key/ Check your Internet Connection as the Website is not getting accessed")
    exit()

news_str = requests.get(url).text
speak("News For Today.... Lets Begin !! ")

# JSON.loads takes a str obj and convert it to a pyobject as per the presence
news = json.loads(news_str)

print(news['status'],news['totalResults'])
print("Total Nubmber of Articles present are ", len(news['articles']))
# Now Looping over the articles of the news
for art in news['articles']:
    print(art['title'])
    speak(art['title'])
    speak("Moving on to the Next news ")