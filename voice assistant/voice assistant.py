#importing important libraries
import pyttsx3  #for text to speech conversion
import datetime  #for date and time operations
import speech_recognition as sr #for speech recognition
import wikipedia  #for fetching information from wikipedia
import webbrowser #for opening web browsers
import os
import subprocess
import platform

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)

def speak(audio):  #function to make the assistant speak
    print("Jarvis:", audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():  #function to greet the user based on the time of day
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How may I help you?")

def takeCommand():  #function to take voice commands from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "none"
    return query.lower()  # make sure it’s always lowercase

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()
        if query == "none" or query.strip() == "":
            continue

        print("Processed query:", query)

        # ✅ broader matching so “open google for me” or “please open google” also works
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't fetch information from Wikipedia.")  


        elif "youtube" in query:   # to open YouTube
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            

        elif "google" in query:   # to open Google
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
            


        elif "stackoverflow" in query or "stack overflow" in query:  # to open Stack Overflow
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")


        

        elif "chatgpt" in query:  #  to open ChatGPT
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")
            
            
        elif "search" in query:  # added a search feature from Google
            search_term = query.replace("search", "").replace("for", "").strip()
            if search_term:
                speak(f"Searching Google for {search_term}")
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
            else:
                speak("Please tell me what to search.")
            
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

         #System apps (Windows)
        elif "open notepad" in query:
            speak("Opening Notepad")
            try:
               if platform.system() == "Windows":
                  subprocess.Popen(["notepad.exe"])
               else:
                  speak("Notepad not supported on this system.")
            except Exception as e:
                 print(e)
                 speak("Unable to open Notepad right now.")

        elif "open calculator" in query:
             speak("Opening Calculator")
             try:
               if platform.system() == "Windows":
                  subprocess.Popen(["calc.exe"])
               else:
                  speak("Calculator not supported on this system.")
             except Exception as e:
               print(e)
               speak("Unable to open Calculator.")
            
            
        elif "quit" in query or "exit" in query or "stop" in query:
            speak("Quitting the program. Have a nice day!")
            break
