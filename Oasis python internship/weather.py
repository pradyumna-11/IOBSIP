import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != 404:
        main_data = data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} Kelvin")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("City Not Found")


api_key = "216525c0a871374f9684cf4105302f90"
city_name = input("Enter city name: ")
get_weather(api_key, city_name)
