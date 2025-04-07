import requests
from os import getenv

WEATHER_API_KEY = getenv("WEATHER_API_KEY")
NEWS_API_KEY = getenv("NEWS_API_KEY")
AIR_RAID_API_KEY = getenv("AIR_RAID_API_KEY")

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def get_currency_rate(base_currency, target_currency):
    response = requests.get(NBU_API_URL)
    if response.status_code != 200:
        return None
    
    data = response.json()
    base_rate = None
    target_rate = None
    
    for item in data:
        if item["cc"] == base_currency:
            base_rate = item["rate"]
        elif item["cc"] == target_currency:
            target_rate = item["rate"]
    
    if base_rate is None or target_rate is None:
        return None
    
    return target_rate / base_rate

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_latest_news():
    url = f"https://newsapi.org/v2/top-headlines?country=ua&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])

def get_air_raid_status():
    url = "https://api.alerts.in.ua/api/alerts/active.json"
    response = requests.get(url)
    data = response.json()
    if data.get("success"):
        return data.get("data", [])
    return None