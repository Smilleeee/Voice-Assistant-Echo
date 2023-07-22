from time import *
import threading
import winsound
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour <5 and hour >=0:
        speak("Hello Master")
    elif hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Friday Please tell me what u want")       

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
        print("please repeat")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

class timer(threading.Thread):
  def __init__(self,s):
    threading.Thread.__init__(self)
    self.msg = f"Setting a timer of {s} sec"
    self.s = s

		# helper function to execute the threads 
  def run(self):
    print(str(self.msg));
    #print(f"Sleeping at {strftime('%X')}")
    sleep(self.s)
    #print(f"Sleep ended at {strftime('%X')}")
    for i in range(0,5):
      for j in range(0,3):
        winsound.Beep(2000, 100)
        sleep(0.01)
      sleep(.75)
    speak("Your time is up , my time is now , you can't see me , my time is now")

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if 'web search' in query:
            speak('Searching Web...')
            query = takeCommand().lower()
            webbrowser.open(query)
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
                

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            webbrowser.open('youtubemusic.com')

        elif 'weather' in query:
            webbrowser.open('accuweather.com')

        elif 'open vs code' in query:
            os.system('code')

        elif'open terminal' in query:
            os.system(os.terminal) 
                 
        elif 'timer' in query:
            speak("How long u want it to beee in seconds ?")
            query = takeCommand().lower()
            s=int(query.split(" ")[0]);
            speak(f"Setting a time for {s} seconds");
            t1=timer(s);
            t1.start();


       
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your email"    
                sendEmail(to, content)
                speak("Email was sent")
            except Exception as e:
                print(e)
                speak("sorry for the inconvience") 
        
        elif 'thank you' in query:
            break