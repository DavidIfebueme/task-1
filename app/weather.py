import requests

def get_weather(city):
    try:
        api_key = '2ca1c0e8c36e7b44a3aada42f0b20f69'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        temperature = weather_data['main']['temp']

        return temperature

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None
