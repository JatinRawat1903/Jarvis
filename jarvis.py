from ntpath import join
from time import struct_time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from time import ctime
from wikipedia.wikipedia import random, search



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1 ].id)
engine.setProperty('voice',voices[1].id)

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("sir please tell me how may i help you")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand(ask=False):
    # it takes microphone input and return string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
         print(ask)
        print("listening....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:-",query)
        #speak (query)
    
    except Exception as e:
        print("Say that again please")
        return "None"
        
        
    return query
    


if __name__=="__main__" :
     wishme()
     while True:
     #if 2:
         #logic for executing result based on query
        query=takecommand().lower()
        if "wikipedia" in query:
            print("Searching in wikipedia...")  
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1) 
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir="d:\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
 
        # elif "the time" in query:
        #     strtime=datetime.datetime.now().strftime("%H:%M:%S")
        #     print(strtime)
        #     speak(f"sir,the time is {strtime}")

        elif "the time" in query:
            # strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(ctime())
            speak(ctime())
        
        elif "open vs code"in query:
            path="C:\\Users\\rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path) 

        elif "what is your name" in query:
            print("SIR MY NAME IS MAAYA")
            speak("SIR MY NAME IS MAAYA")

        elif "exit" in query:
            print("Have a good day")
            speak("Have a good day")
            quit()
        
        elif "search" in query:
            print("what do you want me to search for")
            speak("what do you want me to search for")
            search=takecommand()
            url="https://google.com/search?q=" +search
            webbrowser.get().open(url)
            print(search)
            speak(f"here is the result what is found for{search}")

        elif "find in youtube" in query:
            print("what video you are looking for")
            speak("what video you are looking for")
            video=takecommand()
            url="https://youtube.com/search?q=" +video
            webbrowser.get().open(url)
            print(video)
            speak(f"here is the result what is found for{video}")

        elif "find location" in query:
            print("which place you want me to search for")
            speak("which place you want me to search for")
            location=takecommand()
            url="https://google.nl/maps/place/" +location
            webbrowser.get().open(url)
            print(location)
            speak(f"here is the result what is found for{location}")
        

        elif "what is my name" in query: 
            print("sir your name is Rahul Rawat")
            speak("sir your name is Rahul Rawat")

        elif "who develop you maaya" in query:
            print("Rahul rawat developed me.He gave me this life.I am very thankful to Mr. Rahul Rawat for this")
            speak("Rahul rawat developed me He gave me this life I am very thankful to mr. rahul rawat for this")


            