import os
os.environ["OPENWEATHER_API_KEY"] = "e02d683067a09714f293e2bd5185b37c"
import requests

def main():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print("API KEY =", api_key)
    city = input("Введите название города: ")
    if not city:
        print("Город не  введен")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "mettric",
        "lang": "ru"
    }
    response = requests.get(url, params=params, timeout=15)
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

main()