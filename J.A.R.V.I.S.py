import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import googlesearch
import smtplib
from TimeTable import timetable
from Reminder import remind
from Reminder import take_remind
from Reminder import store_reminder
from Weather import weather_report

#Weather App
#owm = pyowm.OWM('1481183c75501986d143a344d9785a00')
#observation = owm.weather_at_places('Bangalore, India')
#w = observation.get_weather()
# Windows

chrome_path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"

emails = {
    "sameera official" : "sameerajsharma.ec19@rvce.edu.in",
    "sameera unofficial" : "sharmasameera91@gmail.com",
    "roopa" : "ysjtsha@gmail.com",
    "rupa" : "ysjtsha@gmail.com",
    "jayathirtha" : "ysjayathirtha@gmail.com"
    }

engine = pyttsx3.init('sapi5')  #api voices provided by Windows
voices = engine.getProperty('voices')
#print(voices)
# #prints the voices available
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")

    elif hour>=12 and hour<16:
        speak("good afternoon sir!")

    elif hour>=16 and hour<19:
        speak("Good evening Sir!")

    else:
        speak("oh Hello Sir!")

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
            print(e)
            print("Say that again please...")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) #Don't know
    server.ehlo()
    server.starttls() #server is initiated
    server.login('sharmasameera91@gmail.com', 'rjss2205') #To login
    server.sendmail('sharmasameera91@gmail.com', to, content) #sends mail
    server.close()   #Closes the server

def time():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    now = hour + (min / 60)
    return now

if __name__ == "__main__": #main method
    wish_me()
    now = time()
    if now < 10:
        weather_report()
    else:
        speak("how may I help you sir?")
    while(True):
        remind()
        query = takeCommand().lower()
        if 1:
            query = query.replace("sam ", "")
            if "hey" in query:
                query = query.replace("hey ", "")
            if "can you" in query:
                query = query.replace("can you ", "")
            if "for me" in query:
                query = query.replace("for me", "")
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("who is ", "")
                results = wikipedia.summary(query, sentences = 3)
                print("According to Wikipedia: ")
                print(results)
                speak(results)

            elif "show me some videos" in query:
                speak("What is your specific interest today Sir?")
                query = takeCommand()
                speak("I hope this is what you were looking for!")
                stats = query.split()
                if len(stats)==1:
                    webbrowser.get(chrome_path).open(f"youtube.com/results?search_query={stats[0]}")
                elif len(stats)==2:
                    webbrowser.get(chrome_path).open(f"youtube.com/results?search_query={stats[0]}+{stats[1]}")
                elif len(stats)==3:
                    webbrowser.get(chrome_path).open(f"youtube.com/results?search_query={stats[0]}+{stats[1]}+{stats[2]}")
                elif len(stats) == 4:
                    webbrowser.get(chrome_path).open(f"youtube.com/results?search_query={stats[0]}+{stats[1]}+{stats[2]}+{stats[3]}")

            elif "search amazon" in query:
                query = query.replace("search ", "")
                query = query.replace("amazon ", "")
                if "for" in query:
                    query = query.replace("for ", "")
                speak("I hope this is what you were looking for!")
                stats = query.split()
                if len(stats) == 1:
                    webbrowser.get(chrome_path).open(f"amazon.in/s?k={stats[0]}&ref=nb_sb_noss_1")
                elif len(stats) == 2:
                    webbrowser.get(chrome_path).open(f"amazon.in/s?k={stats[0]}+{stats[1]}&ref=nb_sb_noss_1")
                else:
                    webbrowser.get(chrome_path).open(f"amazon.in/s?k={stats[0]}+{stats[1]}+{stats[2]}&ref=nb_sb_noss_1")

            elif "google meet" in query:
                webbrowser.get(chrome_path).open("meet.google.com / landing?authuser = 1")

            elif "flipkart" in query:
                speak("I can do only so much sir!")
                webbrowser.get(chrome_path).open(googlesearch.lucky("Flipkart"))

            elif "amazon" in query:
                speak("I can do only so much sir!")
                webbrowser.get(chrome_path).open(googlesearch.lucky("Amazon"))

            elif "introduce me" in query:
                print("Ok!     Sameera J Sharma, currently studying in the 7th Semester in Electronics and communication engineering at RV College of Engineering. He has a keen interest in embedded system design and firmware development and has been improving himself on the same line. He is also a professional Hindustani Classical flutist and has been learning music since the age of 4. He also recently passed out from National Cadet Corps and was titled the rank of Company sergeant major. He aims to develop himself to become an efficient embedded systems engineer one day and shock the entire world with his talents. ")

                speak("Ok!     Sameera J Sharma, currently studying in the 7th Semester in Electronics and communication engineering at RV College of Engineering. He has a keen interest in embedded system design and firmware development and has been improving himself on the same line. He is also a professional Hindustani Classical flutist and has been learning music since the age of 4. He also recently passed out from National Cadet Corps and was titled the rank of Company sergeant major. He aims to develop himself to become an efficient embedded systems engineer one day and shock the entire world with his talents. ")

            elif "take me to my classes" in query:
                timetable()
                exit()

            elif "remind me" in query:
                if "remind me to" in query:
                    query = query.replace("remind me to ", "")
                if "remind me" in query:
                    query = query.replace("remind me ", "")
                take_remind(query)

            elif "show me my mails" in query:
                speak("Just a moment sir!")
                print("Logging in as sharmasameera@gmail.com")
                webbrowser.get(chrome_path).open("gmail.com")
                continue

            elif "see my mails" in query:
                speak("Just a moment sir!")
                print("Logging in as sharmasameera@gmail.com")
                webbrowser.get(chrome_path).open("gmail.com")
                continue

            elif "search google" in query:
                query = query.replace("search google ","")
                if "for" in query:
                    query=query.replace("for ","")
                speak("I hope this is what you were looking for!")
                stats = query.split()
                if len(stats) == 1:
                    webbrowser.get(chrome_path).open(f"https://www.google.co.in/search?safe=active&ei=HLJ-X6-bJbS38QPl7pmYDw&q=Ashish+chanchlaniu&oq={stats[0]}&gs_lcp=CgZwc3ktYWIQAzIKCC4QyQMQDRCTAjIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToOCAAQ6gIQtAIQmgEQ5QI6CggAELEDEMkDEEM6BAgAEEM6BAguEEM6CAgAELEDEIMBOgUIABCxAzoCCAA6AgguOgcIABDJAxBDOgoILhDHARCjAhBDOg0ILhCxAxDHARCjAhBDOgUILhCxAzoQCC4QxwEQowIQyQMQQxCTAjoHCC4QsQMQQzoNCC4QsQMQyQMQQxCTAjoICC4QsQMQgwE6CwguELEDEMkDEJMCUNaRD1itsg9gu7cPaAFwAXgAgAHWAYgBpBGSAQYzLjE0LjGYAQCgAQGqAQdnd3Mtd2l6sAEGwAEB&sclient=psy-ab&ved=0ahUKEwivmZTKr6TsAhW0W3wKHWV3BvMQ4dUDCA0&uact=5")
                if len(stats) == 2:
                    webbrowser.get(chrome_path).open(f"https://www.google.co.in/search?safe=active&ei=HLJ-X6-bJbS38QPl7pmYDw&q=Ashish+chanchlaniu&oq={stats[0]}+{stats[1]}&gs_lcp=CgZwc3ktYWIQAzIKCC4QyQMQDRCTAjIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToOCAAQ6gIQtAIQmgEQ5QI6CggAELEDEMkDEEM6BAgAEEM6BAguEEM6CAgAELEDEIMBOgUIABCxAzoCCAA6AgguOgcIABDJAxBDOgoILhDHARCjAhBDOg0ILhCxAxDHARCjAhBDOgUILhCxAzoQCC4QxwEQowIQyQMQQxCTAjoHCC4QsQMQQzoNCC4QsQMQyQMQQxCTAjoICC4QsQMQgwE6CwguELEDEMkDEJMCUNaRD1itsg9gu7cPaAFwAXgAgAHWAYgBpBGSAQYzLjE0LjGYAQCgAQGqAQdnd3Mtd2l6sAEGwAEB&sclient=psy-ab&ved=0ahUKEwivmZTKr6TsAhW0W3wKHWV3BvMQ4dUDCA0&uact=5")
                if len(stats) == 3:
                    webbrowser.get(chrome_path).open(f"https://www.google.co.in/search?safe=active&ei=HLJ-X6-bJbS38QPl7pmYDw&q=Ashish+chanchlaniu&oq={stats[0]}+{stats[1]}+{stats[2]}&gs_lcp=CgZwc3ktYWIQAzIKCC4QyQMQDRCTAjIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToOCAAQ6gIQtAIQmgEQ5QI6CggAELEDEMkDEEM6BAgAEEM6BAguEEM6CAgAELEDEIMBOgUIABCxAzoCCAA6AgguOgcIABDJAxBDOgoILhDHARCjAhBDOg0ILhCxAxDHARCjAhBDOgUILhCxAzoQCC4QxwEQowIQyQMQQxCTAjoHCC4QsQMQQzoNCC4QsQMQyQMQQxCTAjoICC4QsQMQgwE6CwguELEDEMkDEJMCUNaRD1itsg9gu7cPaAFwAXgAgAHWAYgBpBGSAQYzLjE0LjGYAQCgAQGqAQdnd3Mtd2l6sAEGwAEB&sclient=psy-ab&ved=0ahUKEwivmZTKr6TsAhW0W3wKHWV3BvMQ4dUDCA0&uact=5")
                if len(stats) == 4:
                    webbrowser.get(chrome_path).open(f"https://www.google.co.in/search?safe=active&ei=HLJ-X6-bJbS38QPl7pmYDw&q=Ashish+chanchlaniu&oq={stats[0]}+{stats[1]}+{stats[2]}+{stats[3]}&gs_lcp=CgZwc3ktYWIQAzIKCC4QyQMQDRCTAjIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDTIECAAQDToOCAAQ6gIQtAIQmgEQ5QI6CggAELEDEMkDEEM6BAgAEEM6BAguEEM6CAgAELEDEIMBOgUIABCxAzoCCAA6AgguOgcIABDJAxBDOgoILhDHARCjAhBDOg0ILhCxAxDHARCjAhBDOgUILhCxAzoQCC4QxwEQowIQyQMQQxCTAjoHCC4QsQMQQzoNCC4QsQMQyQMQQxCTAjoICC4QsQMQgwE6CwguELEDEMkDEJMCUNaRD1itsg9gu7cPaAFwAXgAgAHWAYgBpBGSAQYzLjE0LjGYAQCgAQGqAQdnd3Mtd2l6sAEGwAEB&sclient=psy-ab&ved=0ahUKEwivmZTKr6TsAhW0W3wKHWV3BvMQ4dUDCA0&uact=5")

            elif "listen to me" in query:
                speak("Yes Sir!")

            elif "weather" in query:
                weather_report()

            elif "outside" in query:
                weather_report()

            elif "are you up" in query:
                speak("for you Sir always!")

            elif "are you there" in query:
                speak("for you Sir always!")

            elif 'play some music' in query:
                music_dir = "C:\\Users\\Indusface\\Desktop\\Downloads"
                songs = os.listdir(music_dir)
                print(songs)
                query2 = "no"
                while(query2 == "no"):
                    speak("Are you interested in this song sir?")
                    n = random.randint(0,15)
                    #print(songs[n])
                    speak(songs[n])
                    query2 = takeCommand().lower()
                    if "stop" in query2:
                        break
                if "stop" not in query2:
                    os.startfile(os.path.join(music_dir, songs[n]))   #N is the max songs in the playlist

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, it is {strTime} in Bengaluru, India")

            elif 'who are you' in query:
                speak("You have a nice sense of humour sir!")

            elif "thanks" in query:
                speak("For you, anything sir")

            elif 'create a presentation' in query:
                speak('Sure sir. Opening Microsoft PowerPoint!')
                try:
                    path =  "C:\\Program Files\\Microsoft Office\\Office14\\POWERPNT.exe"
                    os.startfile(path)

                except Exception as e:
                    print(e)
                    speak("Sorry sir, I may be malfunctioning")

            elif "send an email" in query:
                speak("To whom sir?")
                name = takeCommand().lower()
                try:
                    speak("What should I write sir?")
                    content = takeCommand()
                    to = emails[name]
                    sendEmail(to, content)
                    speak("Email has been sent!")

                except Exception as e:
                    print(e)
                    speak("Sorry sir, I think I'm malfunctioning!")

            elif "sing happy" in query:
                speak("I'm H A P P Y!    I'm H A P P Y!    I know I  am I'm sure I  am I'm H A P P Y!")

            elif ("shutdown" or "sleep" or "quit") in query:
                speak("Alright Sir, enjoy your day !")
                speak("")
                exit()