import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyaudio
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am a Voice Assistant created by Animesh how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open browser' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'play music' in query:
            music_dir=r"C:\Users\anime\PycharmProjects\Voice_Assistant\Audio"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%h:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codePath =r"C:\Users\anime\PycharmProjects\Voice_Assistant\main.py"
            os.startfile(codePath)
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "connectanimesh0809@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent Succesfully!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ,I am not able to send this email")
