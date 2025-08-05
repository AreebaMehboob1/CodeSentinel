import requests

# Your API key
API_KEY = "0c116e7813800c5dfa4acc3f18145969"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Ask user for city name
city = input("Enter city name: ").strip()

# Create API request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send request
response = requests.get(url)

# Parse JSON response
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"\n===== Weather in {city.capitalize()} =====")
    print(f"🌡 Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁ Condition: {condition.capitalize()}")

else:
    error_data = response.json()
    print(f"❌ Error: {error_data.get('message', 'Unknown error occurred')}")
