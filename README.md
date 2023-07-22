# Voice-Assistant-Echo
# Description
Echo is a voice assistant built using Python and the Tkinter library for the graphical user interface. It can perform various tasks based on voice commands, including web searches, getting the current time, opening websites, playing music, setting timers, sending emails, and more.

# Features
Voice Interaction: Echo listens to the user's voice commands and responds accordingly.
Greetings: Echo greets the user based on the time of day (morning, afternoon, evening, or night).
Web Search: Users can ask Echo to search the web for any topic.
Time Display: Echo can tell the current time to the user.
Web Browser Integration: Echo can open websites like Google, YouTube, Stack Overflow, and AccuWeather.
Music Player: Echo can open a web page to play music.
Timer: Users can set a timer for a specific duration, and it will notify with a sound when the time is up.
Email Sending: Users can instruct Echo to email a specified address.
Text-to-Speech: Echo uses text-to-speech to communicate with the user.
# Pre-requisites
Python 3.x
Required Python packages: tkinter, threading, datetime, webbrowser, os, smtplib, winsound, pyttsx3, speech_recognition, time.
# How to Use
Make sure you have all the required packages installed.
Run the script echo_voice_assistant.py in a Python environment that supports graphical user interfaces.
The main window of the Echo voice assistant will appear.
Click the "Start Listening" button to activate the voice assistant.
Echo will greet the user based on the time of day and wait for voice commands.
Speak your command, and Echo will execute the corresponding action or provide a response.
# Voice Commands
Web Search: Say "Web search" followed by your search query to perform a web search.
Time Display: Say "What's the time" or similar to get the current time.
Open Websites: Use commands like "Open Google," "Open YouTube," or "Open StackOverflow" to open the corresponding websites.
Music Player: Say "Play music" to open a web page for playing music.
Weather: Use a command like "Weather" to check the weather (opens AccuWeather).
Timer: Say "Set a timer for X seconds" to set a timer, and Echo will notify you when the time is up.
Send Email: Say "Email to me" to instruct Echo to send an email. You need to provide the content of the email during the interaction.
# Note
Echo uses Google's speech recognition service for voice recognition, so a stable internet connection is required.
Make sure to replace the email and password in the sendEmail function with your Gmail credentials to enable email sending
