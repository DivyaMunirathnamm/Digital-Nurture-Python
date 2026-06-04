import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid=YOUR_API_KEY&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 404:
        print("City not found")

    else:
        data = response.json()

        print("Temperature:", data["main"]["temp"])
        print("Condition:", data["weather"][0]["description"])

except requests.exceptions.RequestException:
    print("Network Error")