import requests
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

def get_weather():
    city = input("Enter the city name: ").strip()

    #get the lat and lon of the city
    API_TOKEN = os.getenv("API_KEY")
    geo_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_TOKEN}&units=metric")
    
    if geo_response.status_code != 200:
        print("Error fetching location data.")
        return
    
    geo_data = geo_response.json()

    if not geo_data:
        print("City not found.")
        return
    
    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    #get the weather data of the city

    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_TOKEN}&units=metric")


    if weather_response.status_code != 200:
        print("Error fetching weather data.")
        return
    
    weather_data = weather_response.json()

    if not weather_data:
        print("Weather data not found.")
        return
    
    #get the current date and time in UTC format

    timestamp = weather_data['dt']
    time = datetime.datetime.fromtimestamp(timestamp)
    
    #Print the weather data

    print(f"City: {weather_data['name']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
    print(f"Date and Time: {time} UTC")

get_weather()