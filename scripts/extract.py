import requests

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=41.7151"
    "&longitude=44.8271"
    "&current=temperature_2m,relative_humidity_2m"
)

def get_weather():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()

