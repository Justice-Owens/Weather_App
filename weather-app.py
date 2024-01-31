import requests


def get_weather(api_key, city):

    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geocode_params = {
        'q': city,
        'appid': api_key,
    }

    geocode = requests.get(geocoding_url, params=geocode_params)

    geo_dict = geocode.json()
    first_location = geo_dict[0]

    lat = geo_dict[0]['lat']
    lon = geo_dict[0]['lon']

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None


def kelvin_to_f(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


if __name__ == "__main__":

    api_key = input("Enter your OpenWeather Map API key: ")

    while True:
        city = input("Enter the city name: ")

        while not city or city.isdigit():
            print("Entry was not valid. Please enter a valid city name")
            city = input("Please enter the city name: ")

        weather = get_weather(api_key, city)

        temp_in_k = weather['main']['temp']
        temp_in_f = kelvin_to_f(temp_in_k)

        if weather:
            print(f"Weather in {city}: {weather['weather'][0]['description']}")
            print(f"Temperature: {int(temp_in_f)} °F")
            print(f"Humidity: {weather['main']['humidity']}")
            print(f"Feels Like: {int(kelvin_to_f(weather['main']['feels_like']))} °F")

        ask = input("Would you like to get the weather for another city? Y/N ")
        if ask.lower() == 'n':
            print("Exiting application...")
            break
