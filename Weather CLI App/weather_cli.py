# import requests

# API_KEY = 'ef1168c63359967ac65ea7d2fa382768'
# BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# def get_weather(city):
#     params = {
#         'q': city,
#         'appid': API_KEY,
#         'units': 'metric'  # Celsius
#     }

#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     if data.get('cod') == 200:
#         weather = data['weather'][0]['description']
#         temp = data['main']['temp']
#         feels_like = data['main']['feels_like']
#         humidity = data['main']['humidity']
#         print(f"\n🌤️  Weather in {city.title()}:\n")
#         print(f"Description : {weather}")
#         print(f"Temperature : {temp}°C (feels like {feels_like}°C)")
#         print(f"Humidity    : {humidity}%\n")
#     else:
#         print(f"\n❌ Error: {data.get('message', 'Unable to fetch weather')}\n")

# if __name__ == '__main__':
#     city_name = input("Enter city name: ")
#     get_weather(city_name)
