import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said : {query}")
            return query
        except Exception as e:
            print("Some Error:", e)
            return "Some Error"


print("Listening")
speaker.Speak("Hello Aaditya Sir ! How may i help you")
text = takeCommand()
sites = [
    ["Youtube", "https://www.youtube.com"],
    ["education", "https://markeducation.netlify.app"],
    ["Google", "https://www.google.com"],
    ["Amazon", "https://www.amazon.com"],
    ["Facebook", "https://www.facebook.com"],
    ["Twitter", "https://twitter.com"],
    ["Reddit", "https://www.reddit.com"],
    ["GitHub", "https://github.com"],
    ["Wikipedia", "https://www.wikipedia.org"],
    ["Netflix", "https://www.netflix.com"],
    ["Instagram", "https://www.instagram.com"],
    ["LinkedIn", "https://www.linkedin.com"],
    ["Stack Overflow", "https://stackoverflow.com"],
    ["Microsoft", "https://www.microsoft.com"],
    ["Apple", "https://www.apple.com"],
    ["CNN", "https://www.cnn.com"],
    ["BBC", "https://www.bbc.com"],
    ["Yahoo", "https://www.yahoo.com"],
    ["Quora", "https://www.quora.com"],
    ["Etsy", "https://www.etsy.com"],
    ["Walmart", "https://www.walmart.com"],
    ["Adobe", "https://www.adobe.com"],
    ["eBay", "https://www.ebay.com"],
    ["Pinterest", "https://www.pinterest.com"],
    ["WordPress", "https://wordpress.com"],
]

for site in sites:
    if f"Open {site[0]}".lower() in text.lower():
        speaker.Speak(f"Opening {site[0]}")
        webbrowser.open(site[1])
        speaker.Speak("Have a Great Day Sir !")
if "the time" in text:
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    speaker.Speak(f"Sir the time is {strfTime}")
