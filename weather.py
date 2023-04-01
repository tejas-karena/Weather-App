import tkinter as tk
import requests


API_KEY = "30d4741c779ba94c470ca1f63045390a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city_name):
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"{city}: {temperature}°C, {description}"
    else:
        return "There is Some error"

def show_weather_data():
    city_name = city_entry.get()
    weather_data = get_weather_data(city_name)
    weather_label.config(text=weather_data)


win = tk.Tk()
win.title("Weather App")
win.configure(bg='lightblue')


city_frame = tk.Frame(win)
city_frame.grid(row=0, column=0, padx=10, pady=10)

city_label = tk.Label(city_frame, text="Enter city name:", font=("Time New Roman", 14))
city_label.grid(row=0, column=0, padx=5)

city_entry = tk.Entry(city_frame, font=("Time New Roman", 14))
city_entry.grid(row=0, column=1, padx=5)

show_weather_button = tk.Button(win, text="Show Weather", command=show_weather_data, font=("Time New Roman", 14), padx=10)
show_weather_button.grid(row=1, column=0, pady=10)

weather_label_frame = tk.Frame(win)
weather_label_frame.grid(row=2, column=0, padx=10, pady=10)

weather_label_title = tk.Label(weather_label_frame, text="Weather Data:", font=("Time New Roman", 16, "bold"))
weather_label_title.pack(side="left", padx=5, pady=5)

weather_label = tk.Label(weather_label_frame, text="", font=("Time New Roman", 16), justify="left", padx=10, pady=10)
weather_label.pack(side="left", padx=5, pady=5)

win.mainloop()
