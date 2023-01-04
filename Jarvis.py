import pyttsx3  # pip instal pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import time  # wikipedia ,webbrowser,subprocess, sys, os, smtplib, re, requests, youtube_dl, json, time, random, pyaudio
from pyowm import OWM
from bs4 import BeautifulSoup as soup
from time import strftime
from selenium import webdriver
from gtts import gTTS
import speech_recognition as sr

MASTER = "Raghava"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
print("I'm Listening")
#speak function will pronounce the string which is passed to it
def speak(text):
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)
    engine.setProperty('pitch', 32)
    engine.say(text)
    engine.runAndWait()
speak("Ready to go")
# This function will wish you looking at the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("How may I help you")
    
def sleep():
    time.sleep(5)
    
def timer():
    strTime = datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
    
    speak(f"Sir, the time is {strTime}")
    print(strTime)
#     speak("Do u need anything else sir")
    return strTime

def mainfunction(source):
    print("1")
    r.adjust_for_ambient_noise(source)
    print("2")
    r.pause_threshold = 1 #seconds of non-speaking audio before a phrase is considered complete
    print("3")
    audio = r.listen(source)
    print("4")
    print(audio)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print("Could you please say that again ?")
        speak("Could you please say that again ?")
        return 0

    print("User Command: ",query)
    
    if "time" in query:
        timer()
        
    elif 'open Google Chrome' in query:
        driver = webdriver.Chrome(r"C:\\Users\\spsoft\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
        driver.implicitly_wait(1)
        driver.maximize_window()
        driver.get("https://www.google.com/")
        
    elif 'Google' in query:
        driver = webdriver.Chrome(r"C:\\Users\\spsoft\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
        driver.implicitly_wait(1)
        driver.maximize_window()  
        indx = query.split().index('Google')
        query_ = query.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query_))
        return
  
    elif 'search' in query:
        driver = webdriver.Chrome(r"C:\\Users\\spsoft\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
        driver.implicitly_wait(1)
        driver.maximize_window()
        indx = query.split().index('search')
        query_ = query.split()[indx + 1:]
        driver.get("https://www.google.com/search?q=" + '+'.join(query_))
        return
    
    elif 'open Youtube' in query:
        driver = webdriver.Chrome(r"C:\\Users\\spsoft\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver.exe")
        driver.implicitly_wait(1)
        driver.maximize_window()
        indx = query.split().index('youtube')
        query_ = query.split()[indx + 1:]
        print(query_)
        driver.get("https://www.youtube.com/results?search_query=" + '+'.join(query_))
        return
    
    elif 'shutdown' in query:
            speak(f'sir, Jarvis is shutdowning')
            exit

    else:
        print("Helloo: ",query)
        
if __name__ == "__main__":
    r = sr.Recognizer()
    wishMe()
    with sr.Microphone() as source:
        while 1:
#             query = takeCommand().lower()
            mainfunction(source)

    