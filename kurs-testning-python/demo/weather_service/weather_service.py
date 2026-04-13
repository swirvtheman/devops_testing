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
        data = response.json()
        return data["temperature"]

