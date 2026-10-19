import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def _get(self, endpoint, params):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError):
            return None

    def get_current_weather(self, location):
        params = {"key": self.api_key, "q": location}
        return self._get("current.json", params)

    def get_forecast(self, location, days=3):
        if days < 1 or days > 3:
            raise ValueError("days must be between 1 and 3")
        params = {"key": self.api_key, "q": location, "days": days}
        return self._get("forecast.json", params)


def format_current_weather(data):
    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_f"]
    condition = data["current"]["condition"]["text"]
    return f"{city}, {country}: {temp}°F, {condition}"


def format_forecast(data):
    lines = []
    for day in data["forecast"]["forecastday"]:
        date = day["date"]
        high = day["day"]["maxtemp_f"]
        low = day["day"]["mintemp_f"]
        condition = day["day"]["condition"]["text"]
        lines.append(f"{date}: high {high}°F, low {low}°F, {condition}")
    return "\n".join(lines)