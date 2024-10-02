import datetime
import os
import webbrowser
import openai
import subprocess
import psutil
import pyttsx3
import speech_recognition as sr
import pyautogui  # For window management
import pyperclip  # For clipboard control
from config import apikey
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

chatStr = ""

def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Amit: {query}\n Useless: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = response["choices"][0]["text"].strip()
    say(reply)
    chatStr += f"{reply}\n"
    return reply

def ai(prompt):
    openai.api_key = apikey
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ai_response = response.choices[0].text.strip()
    say(ai_response)
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{prompt[:30].strip()}.txt", "w") as f:
        f.write(ai_response)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You: {query}")
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry from Useless"

# Feature 1: Control Volume
def change_volume(command):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if "mute" in command:
        volume.SetMute(1, None)
        say("Volume muted")
    elif "unmute" in command:
        volume.SetMute(0, None)
        say("Volume unmuted")
    elif "increase" in command:
        current_volume = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(current_volume + 2.0, None)
        say("Volume increased")
    elif "decrease" in command:
        current_volume = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(current_volume - 2.0, None)
        say("Volume decreased")

# Feature 2: Open Applications
def open_application(command):
    if "notepad" in command:
        subprocess.Popen("notepad.exe")
        say("Opening Notepad")
    elif "calculator" in command:
        subprocess.Popen("calc.exe")
        say("Opening Calculator")
    elif "chrome" in command:
        subprocess.Popen("chrome.exe")
        say("Opening Google Chrome")

# Feature 3: Close Applications
def close_application(command):
    if "notepad" in command:
        for proc in psutil.process_iter():
            if proc.name() == "notepad.exe":
                proc.terminate()
                say("Closing Notepad")

# Feature 4: Open Folders
def open_folder(command):
    if "documents" in command:
        documents_path = os.path.expanduser("~/Documents")
        os.startfile(documents_path)
        say("Opening Documents folder")
    elif "downloads" in command:
        downloads_path = os.path.expanduser("~/Downloads")
        os.startfile(downloads_path)
        say("Opening Downloads folder")

# Feature 5: System Control (Shutdown, Restart, Log Off)
def system_control(command):
    if "shutdown" in command:
        say("Shutting down the system")
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        say("Restarting the system")
        os.system("shutdown /r /t 1")
    elif "log off" in command:
        say("Logging off the system")
        os.system("shutdown /l")

# Feature 6: Clipboard Interaction
def clipboard_interaction(command):
    if "copy" in command:
        pyautogui.hotkey("ctrl", "c")
        say("Content copied to clipboard")
    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")
        say("Pasting clipboard content")
    elif "show clipboard" in command:
        clipboard_content = pyperclip.paste()
        say(f"Clipboard content: {clipboard_content}")

# Feature 7: Window Management (Minimize, Maximize, Switch)
def manage_windows(command):
    if "minimize" in command:
        pyautogui.hotkey("win", "down")
        say("Window minimized")
    elif "maximize" in command:
        pyautogui.hotkey("win", "up")
        say("Window maximized")
    elif "switch" in command:
        pyautogui.hotkey("alt", "tab")
        say("Switching window")

# Feature 8: Google Search
def google_search(query):
    search_query = query.replace("search", "").strip()
    url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(url)
    say(f"Searching Google for {search_query}")

# Main loop for listening to commands and performing tasks
say("Jai Shree Raam, I am Useful Life Enhancing Software System, AKA Useless Version 1")

while True:
    query = listen()

    # Check for volume control commands
    if "volume" in query:
        change_volume(query)

    # Check for application opening commands
    elif "open" in query:
        open_application(query)

    # Check for application closing commands
    elif "close" in query:
        close_application(query)

    # Check for folder opening commands
    elif "open folder" in query:
        open_folder(query)

    # Check for system control commands
    elif "shutdown" in query or "restart" in query or "log off" in query:
        system_control(query)

    # Check for clipboard interaction
    elif "clipboard" in query:
        clipboard_interaction(query)

    # Check for window management commands
    elif "window" in query:
        manage_windows(query)

    # Check for Google search commands
    elif "search" in query:
        google_search(query)

    # Other interactions and conversations
    elif "if I die then will you guide my team" in query:
        say("You crafted me for this very purpose, and I'll faithfully carry out my duties, boss.")

    elif "go to sleep mode" in query:
        say("Entering Sleep Mode. Say Hey Useless to wake me up!")
        say("Say 'uth jaa bhai'")

    elif "what do you think about ChatGPT" in query:
        say("le moot diyaa tere ChatGPT pe")

    elif "who created you" in query:
        say("Amit Kasabe")

    elif "tell me about Amit Kasabe" in query:
        say("Amit Kasabe is a 22-year-old cybersecurity student...")

    elif "tell me about sanatan" in query:
        say("Sanatan Dharma is the oldest dharma in the world.")

    elif "quit" in query.lower():
        say("Quitting")
        exit()

    # AI-based query
    elif "useless" in query.lower():
        ai(query)

    else:
        chat(query)

    # Reset chat conversation
    if "reset chat" in query.lower():
        chatStr = " "
