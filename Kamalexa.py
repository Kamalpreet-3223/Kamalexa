import datetime
import os
import webbrowser

import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour > 0 and hour < 12):
        speak("Good Morning!")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am Kamalexa here . Please tell me How may I help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        try:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                print(results)
                speak("According to wikipedia")
                speak(results)

            ##            elif 'experiment' in query:                               ## THIS IS DOING THE SAME THING AS THE ABOVE WIKIPEDIA IS DOING
            ##                query = query.replace('experiment' , '')
            ##                pywhatkit.info(query , lines = 2)


            elif 'play' in query:
                query = query.replace('play', '')
                pywhatkit.playonyt(query)
                print("Playing...")
                speak("Playing...")


            elif 'play music' in query:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The time is {strTime}\n")

            elif 'open code' in query:
                codePath = "C:\\Users\\Kamalpreet Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open linkedin' in query:
                webbrowser.open("https://www.linkedin.com/in/kamalpreet-singh-8558131a0/")
                speak("Opening your linked account")

            elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com/profile.php?id=100014358135907")
                speak("Opening Facebook")

            
            elif 'open instagram' in query:
                webbrowser.open("https://www.instagram.com/kamalpreet__singh__/")
                speak("Opening Instagram")

            elif 'how are you' in query:
                speak("Sir I am Great")

            elif 'your name' in query:
                speak("Sir my name is Kamalexa")

            elif 'search' in query:
                query = query.replace("search", "")
                webbrowser.open(f"https://www.google.com/search?q=${query}")
            
            elif 'tell me something funny' in query:
                joke = speak(pyjokes.get_joke())
                print(joke)

        except Exception as e:
            print(e)
