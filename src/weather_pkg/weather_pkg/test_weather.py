import os
import requests

def get_weather(city):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY', None)
    if not api_key:
        return f"API key is missing for {city}!"

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f"Weather in {city}:\nTemperature: {temperature:.1f}°C\nCondition: {description.capitalize()}"
        else:
            return f"Failed to get weather data for {city}: {data.get('message', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return f"Failed to get weather data for {city}: {e}"

if __name__ == "__main__":
    city = "Tokyo"
    weather_info = get_weather(city)
    print(weather_info)
