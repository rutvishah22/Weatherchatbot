import requests
import json
import speech_recognition as sr
import win32com.client

print("WELCOME TO MYCITYWEATHER🌎")

city = print("Which city weather do you want? ")
recognizer = sr.Recognizer() #initializing recognizer object

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")

url = f"https://api.weatherapi.com/v1/current.json?key=97f9c6205da44ec296932112240106&q={text}"
r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text) #convertig string into dic
countr = wdic["location"]["country"]
temp = wdic["current"]["temp_c"]
cond = wdic["current"]["condition"]["text"]

tempfinal = f"The current temperature in {text}, {countr} is {temp} degree celsius."

deg = f"Currently \n  {temp}\n"
toprint = f" {text}, {countr}\n"
conprint = f" {cond}"

speaker = win32com.client.Dispatch("SAPI.SpVoice") #initialize
print(deg, toprint, conprint)
speaker.Speak(tempfinal)




