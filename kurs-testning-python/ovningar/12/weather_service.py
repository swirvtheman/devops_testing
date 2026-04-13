import requests


class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weather.com"

    def get_temperature(self, city):
        response = requests.get(
            f"{self.base_url}/current",
            params={"city": city, "key": self.api_key}
        )
        response.raise_for_status()
        return response.json()["temperature"]

    def get_forecast(self, city, days=5):
        response = requests.get(
            f"{self.base_url}/forecast",
            params={"city": city, "days": days, "key": self.api_key}
        )
        response.raise_for_status()
        return response.json()["forecast"]
