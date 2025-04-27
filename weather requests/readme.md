# Weather App

A simple command-line Python application that fetches and displays current weather information for any city using the OpenWeatherMap API.

## Features

- Get real-time weather data for any city worldwide
- Display temperature in Celsius
- Show current weather conditions
- Show current date and time of the weather data

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/shihabhasan0161/weather-app.git
   cd weather-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   API_KEY = your_api_key_here
   ```

## Usage

Run the application using Python:

```bash
python weather.py
```

When prompted, enter the name of the city you want to check the weather for.

## How It Works

The application:
1. Takes a city name as input from the user
2. Uses OpenWeatherMap's Geocoding API to convert the city name to latitude and longitude
3. Fetches current weather data using those coordinates
4. Displays the city name, current temperature, weather description, and timestamp

## Dependencies

- requests: For making HTTP requests to the OpenWeatherMap API
- python-dotenv: For loading environment variables from the .env file

## API Reference

This application uses the [OpenWeatherMap API](https://openweathermap.org/api):
- Geocoding API to get city coordinates
- Current Weather Data API to get weather information