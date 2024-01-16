import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
import webbrowser
import pyautogui

#initializing the speech engine - setting the voice property and other things 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#wish me wishes the user
def WishMe():
    speak("Hello master This is parul nayak. All the processes are initializing.")
    time.sleep(1)
    speak("The system is now online, ready to take commands.")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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
    WishMe()

    while True:
        query = takecommand().lower()

        if "search" in query:
            search_query = query.replace("search", "").strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching for {search_query}.")

        elif "close tab" in query:
            pyautogui.hotkey('ctrl', 'w')
            speak("Closing the current tab.")
        elif "scroll up" in query:
            pyautogui.scroll(5)
        elif "scroll down" in query:
            pyautogui.scroll(-5)
        elif "click" in query:
            pyautogui.leftClick()
        elif "control the mouse using my hand" in query:
            import mcont
        elif "stop controlling the mouse" in query:
            pyautogui.hotkey("esc")
        elif "exit" in query:
            speak("Exiting the command loop.")
            break