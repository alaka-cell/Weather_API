from dotenv import load_dotenv
import os
import requests

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str):
    if not WEATHER_API_KEY:
        return {"error": "No API key found in .env file"}

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch weather. Code: {response.status_code}"}

    try:
        data = response.json()
        current = data.get("current", {})
        return {
            "city": city,
            "condition": current.get("condition", {}).get("text", "Unknown"),
            "temp_c": current.get("temp_c", "Unknown"),
            "humidity": current.get("humidity", "Unknown"),
        }
    except Exception as e:
        return {"error": f"Error parsing response: {str(e)}"}
