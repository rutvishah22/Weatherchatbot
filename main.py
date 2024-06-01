import requests #used to bring data over the networks
import json #used to work with json data
import win32com.client

print("WELCOME TO MYCITYWEATHER")
city = input("Enter the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=97f9c6205da44ec296932112240106&q={city}"
r= requests.get(url)
# print(r.text)  #type = string

#now we have to convert str into ditcionary sothat we can access its data
wdic = json.loads(r.text)
countr = wdic["location"]["country"]
w= wdic["current"]["temp_c"]
cond = wdic["current"]["condition"]["text"]

#final things that we wanna list
countrfinal = f"Country: {countr}\n"
final = f"Current weather in {city} is {w} degree celsius."
condfinal = f"\nCurrently {cond}"

speaker = win32com.client.Dispatch("SAPI.SpVoice") #initialize
print(countrfinal)
speaker.Speak(final)
speaker.Speak(condfinal)
print(final, condfinal)

