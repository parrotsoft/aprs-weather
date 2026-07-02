import json
from urllib.request import urlopen, Request


class OpenWeatherMap:
    def __init__(self, api_key: str, city: str, country: str):
        self.api_key = api_key
        self.city = city
        self.country = country

    def get_temperature_celsius(self) -> float:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city},{self.country}"
            f"&APPID={self.api_key}"
        )
        req = Request(url, headers={"User-Agent": "aprs-weather/1.0"})
        response = urlopen(req, timeout=10)
        data = json.loads(response.read().decode())
        return data["main"]["temp"] - 273.15
