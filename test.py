from tkinter import *
from threading import Thread
import datetime
import webbrowser
import os
import smtplib
import winsound
import pyttsx3
import speech_recognition as sr
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 5 and hour >= 0:
        speak("Hello Master")
    elif hour >= 5 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Echo. Please tell me what you want.")


def takeCommand():
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
        print("Please repeat")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


class Timer(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.msg = f"Setting a timer of {s} sec"
        self.s = s

    def run(self):
        print(str(self.msg))
        time.sleep(self.s)
        for i in range(0, 5):
            for j in range(0, 3):
                winsound.Beep(2000, 100)
                time.sleep(0.01)
            time.sleep(0.75)
        speak("Your time is up, my time is now, you can't see me, my time is now")


def handle_web_search():
    speak('Searching Web...')
    query = takeCommand().lower()
    webbrowser.open(query)


def handle_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")


def open_google():
    webbrowser.open("https://www.google.com")


def open_youtube():
    webbrowser.open("https://www.youtube.com")


def open_stackoverflow():
    webbrowser.open("https://stackoverflow.com")


def play_music():
    webbrowser.open('https://www.youtube.com/music')


def handle_weather():
    webbrowser.open('https://www.accuweather.com')


def open_vs_code():
    os.system('code')


def open_terminal():
    os.system(os.terminal)


def handle_email():
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "theemailyouwant@gmail.com"
        sendEmail(to, content)
        speak("Email was sent")
    except Exception as e:
        print(e)
        speak("Sorry for the inconvenience")


# Create the main window
window = Tk()
window.title("Echo")
window.geometry("400x500")
window.configure(bg="#F0F0F0")

# Create labels
label = Label(window, text="Welcome to Echo", font=("Arial", 20, "bold"), fg="#333333", bg="#F0F0F0")
label.pack(pady=20)

output_frame = Frame(window, bg="#FFFFFF")
output_frame.pack(pady=10)

output_scroll = Scrollbar(output_frame)
output_scroll.pack(side=RIGHT, fill=Y)

output = Text(output_frame, width=40, height=10, font=("Arial", 12), bd=0, wrap=WORD, yscrollcommand=output_scroll.set)
output.pack()

output_scroll.config(command=output.yview)

# Function to update the output text
def update_output_text(text):
    output.insert(END, text + "\n")
    output.see(END)

# Function to handle button click
def on_button_click():
    output.delete(1.0, END)  # Clear the output text
    thread = Thread(target=handle_commands)
    thread.start()

# Function to handle commands
def handle_commands():
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'thank you' in query:
            update_output_text("Goodbye!")
            break
        update_output_text("User said: " + query)

        # Add your logic to handle different commands and update the output accordingly

        if 'web search' in query:
            handle_web_search()
        elif 'the time' in query:
            handle_time()
        elif 'open google' in query:
            open_google()
        elif 'open youtube' in query:
            open_youtube()
        elif 'open stackoverflow' in query:
            open_stackoverflow()
        elif 'play music' in query:
            play_music()
        elif 'weather' in query:
            handle_weather()
        elif 'open vs code' in query:
            open_vs_code()
        elif 'open terminal' in query:
            open_terminal()
        elif 'timer' in query:
            update_output_text("How long do you want the timer to be in seconds?")
            query = takeCommand().lower()
            s = int(query.split(" ")[0])
            update_output_text(f"Setting a timer for {s} seconds")
            t1 = Timer(s)
            t1.start()
        elif 'email to me' in query:
            handle_email()

# Create a button
button = Button(window, text="Start Listening", font=("Arial", 14, "bold"), bg="#333333", fg="#FFFFFF", relief=FLAT,
                command=on_button_click)
button.pack(pady=20)

# Start the main loop
window.mainloop()
