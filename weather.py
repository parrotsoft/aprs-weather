import json
from typing import Any
from urllib.request import urlopen, Request


class OpenWeatherMap:
    def __init__(self, api_key: str, city: str, country: str):
        self.api_key = api_key
        self.city = city
        self.country = country

    def _fetch(self) -> dict[str, Any]:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={self.city},{self.country}"
            f"&APPID={self.api_key}"
        )
        req = Request(url, headers={"User-Agent": "aprs-weather/1.0"})
        response = urlopen(req, timeout=10)
        return json.loads(response.read().decode())

    def get_temperature_celsius(self) -> float:
        return self._fetch()["main"]["temp"] - 273.15

    def get_all(self) -> dict[str, Any]:
        data = self._fetch()
        main = data["main"]
        wind = data.get("wind", {})
        weather_desc = data["weather"][0]["description"] if data.get("weather") else ""

        return {
            "city": self.city,
            "temp_c": main["temp"] - 273.15,
            "feels_like": main["feels_like"] - 273.15,
            "humidity": main.get("humidity"),
            "pressure": main.get("pressure"),
            "wind_speed": wind.get("speed"),
            "wind_deg": wind.get("deg"),
            "gust": wind.get("gust"),
            "weather_desc": weather_desc,
        }
