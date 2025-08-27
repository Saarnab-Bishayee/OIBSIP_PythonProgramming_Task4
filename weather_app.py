import requests
from Voice_Assistant import pns, listen

API_KEY = "<Your-API-Key>"
pns("Tell the city name whose weather to search:")
CITY = listen()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

params = {"q": CITY,"appid": API_KEY,"units": "metric"}
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    weather_type = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    pns(f"Weather in {city}, {country}:")
    pns(f"Temperature: {temp}°C")
    pns(f"Feels like: {feels_like}°C")
    pns(f"Minimum Temperature: {min_temp}°C")
    pns(f"Maximum Temperature: {max_temp}°C")
    pns(f"Weather Type: {weather_type}")
    pns(f"Weather Condition: {weather_desc.title()}")
    pns(f"Humidity: {humidity}%")
    pns(f"Wind Speed: {wind_speed} metres per second")
    pns("Thank you for using our free Weather App!\nPlease do visit again.")
else:
    pns(f"Error fetching data!\nStatus Code: {response.status_code}")