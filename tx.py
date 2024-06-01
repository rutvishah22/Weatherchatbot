import requests
import json
import win32com.client
import tkinter as tk
from tkinter import messagebox


def get_weather():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=97f9c6205da44ec296932112240106&q={city}"
    r = requests.get(url)

    if r.status_code == 200:
        wdic = json.loads(r.text)
        country = wdic["location"]["country"]
        temperature = wdic["current"]["temp_c"]
        condition = wdic["current"]["condition"]["text"]

        countrfinal = f"Country: {country}"
        final = f"Current weather in {city} is {temperature}°C."
        condfinal = f"Condition: {condition}"

        speaker.Speak(final)
        speaker.Speak(condfinal)

        result_label.config(text=countrfinal + "\n" + final + "\n" + condfinal)
    else:
        messagebox.showerror("Error", "City not found.")


speaker = win32com.client.Dispatch("SAPI.SpVoice")

root = tk.Tk()
root.title("MyCityWeather")

label = tk.Label(root, text="Enter the city:", font=("Arial", 14))
label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
