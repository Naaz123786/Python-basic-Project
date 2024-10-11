import requests


def get_weather(city_name):
    api_key = 'd575ef109b875ddb7c8337d914f92b12'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=d575ef109b875ddb7c8337d914f92b12&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Error: Unable to retrieve weather data for {city_name}.")


# Example usage:
city_name = input("Enter city name: ")
get_weather(city_name)