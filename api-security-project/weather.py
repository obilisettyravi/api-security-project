"""
weather.py -- Secure, production-ready OpenWeatherMap client.

Fixes applied:
  Task 1: API key loaded from .env via python-dotenv (never hardcoded).
  Task 2: HTTP 429 / 401 / 404 handled explicitly -- no KeyError crash.
  Task 3: City name NOT logged (GDPR Art.5(1)(c) / HIPAA s164.502(b)).
"""

import os
import requests
from dotenv import load_dotenv

# Task 1 -- Load API key from environment, not from source code
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise EnvironmentError(
        "OPENWEATHER_API_KEY is not set. "
        "Add it to your .env file and never commit that file."
    )

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> dict | None:
    """Fetch current weather for a city and return parsed JSON, or None."""

    # Task 3 -- REMOVED: print(f"Fetching weather for: {city}...")
    #
    # City is the user's location data. Logging it violates:
    #   - GDPR Article 5(1)(c): data minimisation -- do not process more
    #     personal data than strictly necessary for the service.
    #   - HIPAA Minimum Necessary Rule s164.502(b): limit use/disclosure
    #     of PHI to the minimum required for the purpose.
    # Logging location data for clinic patients creates a privacy audit
    # liability and must be avoided under company policy.

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to the weather service.")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None

    # Task 2 -- Explicit status-code checking (no KeyError crash on 429)
    if response.status_code == 200:
        return response.json()

    elif response.status_code == 429:
        print(
            "Error: Rate limit exceeded (60 calls/min on free tier). "
            "Please wait one minute before trying again."
        )
        return None

    elif response.status_code == 401:
        print("Error: Invalid or missing API key. Check your .env file.")
        return None

    elif response.status_code == 404:
        print("Error: City not found. Please check the spelling.")
        return None

    else:
        print(f"Error: Unexpected HTTP {response.status_code}.")
        return None


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if not city:
        print("No city entered.")
    else:
        data = get_weather(city)
        if data:
            main    = data.get("main", {})
            weather = data.get("weather", [{}])[0]
            print(f"Temperature : {main.get('temp')} C")
            print(f"Feels like  : {main.get('feels_like')} C")
            print(f"Humidity    : {main.get('humidity')}%")
            print(f"Condition   : {weather.get('description', '').title()}")
