import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import googlesearch
import smtplib

chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    '''


    '''
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recogising...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)
            print("Say that again please...")
            return "None"
        return query

def take_remind(reminder):

    try:
        os.remove("remind.txt")
    except:
        pass

    speak("When should I remind you sir?")
    time_str = takeCommand()
    time = 0
    if "a.m." in time_str:
        time_str = time_str.replace(" a.m.", "")
        if len(time_str)==4:
            time = int(time_str[0])+(((int(time_str[2])*10)+int(time_str[3]))/60)
        if len(time_str)==5:
            time = ((int(time_str[0])*10)+int(time_str[1]))+(((int(time_str[3])*10)+int(time_str[4]))/60)
    elif "p.m." in time_str:
        time_str = time_str.replace(" p.m.", "")
        if len(time_str)==4:
            time = (int(time_str[0])+12)+(((int(time_str[2])*10)+int(time_str[3]))/60)
        if len(time_str)==5:
            time = ((int(time_str[0])*10)+int(time_str[1])+12)+(((int(time_str[3])*10)+int(time_str[4]))/60)
    store_reminder(reminder, time)
    speak("I will remind you sir!")
    return reminder

def store_reminder(reminder, time):
    try:
        os.remove("remind.txt")
    except:
        speak("")
    remind_txt = open("remind.txt", "w+")
    remind_txt.write(reminder+"\n")
    remind_txt.write(str(time))
    remind_txt.close()

def remind():
    reminds = open("remind.txt", "r")
    contents = reminds.readlines()
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    now = hour + (min / 60)
    time = contents[1]
    i=0
    if str(now)==time:
        while (i < 5):
            speak("Reminder Alert: "+contents[0])
            i+=1
    if i==5:
        reminds.close()
        reminds = open("remind.txt","w+")
        reminds.write("nothing\n")
        reminds.write("0")