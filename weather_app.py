import requests

API_KEY = 'your_api_key_here'

def fetch_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        temperature = main_data['temp'] - 273.15  # Convert Kelvin to Celsius
        humidity = main_data['humidity']
        weather_description = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
    else:
        print("City not found. Please try again.")

def main():
    city = input("Enter the city name: ")
    weather_data = fetch_weather_data(city)
    display_weather_data(weather_data)

if _name_ == "_main_":
    main()
