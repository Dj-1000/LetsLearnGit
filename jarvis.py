import sys
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
#engine.setProperty('rate')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# today = datetime.datetime.today()
# today = today.strftime("%B %d, %Y")
#print (today.strftime("%B %d, %Y"))
def wishme():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good morning!")
    elif hour>=0 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am Jarvis. How may I help you?") 

def takeCommand():
    cmd = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        source.pause_threshold = 1
        audio = cmd.listen(source)

    try:
        print("Recognizing...")
        query = cmd.recognize_google(audio,language = 'en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        print("Can you say that again please!...")
        takeCommand()

    return query



if __name__ == '__main__':
    wishme()
    # while True
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching wikepedia...")
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query , sentences = 2)
        speak("According to wikipedia: ")
        print(f"Results : {results}")
        speak(results)

    elif 'youtube' in query:
        webbrowser.open("www.youtube.com")
    elif 'open google' in query:
        webbrowser.open("www.google.com")

    elif 'spotify'  in query:
        spotify = "C:\\Users\\djsha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
        os.startfile(spotify)

    elif 'send a mail' in query:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,  the time is %s"  % strTime)

    
        
    
       



