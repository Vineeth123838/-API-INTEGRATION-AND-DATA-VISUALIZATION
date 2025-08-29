import requests
import matplotlib.pyplot as plt

# Paste your OpenWeatherMap API key here 👇
API_KEY = "e5678455ab5df645ec243ceb3e5dc15c"
CITY = "khammam"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data
response = requests.get(url)
data = response.json()

# Extract temperature and dates
dates = [item['dt_txt'] for item in data['list']]
temps = [item['main']['temp'] for item in data['list']]

# Plot graph
plt.figure(figsize=(12,6))
plt.plot(dates, temps, marker="o")
plt.xticks(rotation=45)
plt.title(f"Weather Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
