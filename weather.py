from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

# -------------------------------
# Step 1: Scrape weather data
# -------------------------------

# Example webpage (you can replace this URL with a real one)
url = "https://example.com/daily-weather"

# For demonstration, we’ll simulate a small HTML page
html_data = """
<html>
<body>
  <div class="weather">
    <div class="day">
      <span class="date">2025-11-06</span>
      <span class="temp">36</span>
      <span class="condition">Sunny</span>
    </div>
    <div class="day">
      <span class="date">2025-11-05</span>
      <span class="temp">32</span>
      <span class="condition">Cloudy</span>
    </div>
    <div class="day">
      <span class="date">2025-11-04</span>
      <span class="temp">38</span>
      <span class="condition">Hot</span>
    </div>
  </div>
</body>
</html>
"""

# In a real case, you would use:
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

soup = BeautifulSoup(html_data, "html.parser")

weather_data = []

for day in soup.find_all("div", class_="day"):
    date_tag = day.find("span", class_="date")
    temp_tag = day.find("span", class_="temp")
    cond_tag = day.find("span", class_="condition")

    if date_tag and temp_tag and cond_tag:
        date = date_tag.get_text(strip=True)
        temp = int(temp_tag.get_text(strip=True))
        condition = cond_tag.get_text(strip=True)

        weather_data.append({
            "date": date,
            "temperature": temp,
            "condition": condition
        })

print("Scraped Weather Data:")
for record in weather_data:
    print(record)

# -------------------------------
# Step 2: Store data in MongoDB
# -------------------------------

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["weatherDB"]
collection = db["daily_weather"]

# Clear existing data (for demo)
collection.delete_many({})

# Insert new scraped data
collection.insert_many(weather_data)

print("\nData inserted into MongoDB successfully.")

# -------------------------------
# Step 3: Query temperatures > 35°C
# -------------------------------

query = {"temperature": {"$gt": 35}}
hot_days = collection.find(query)

print("\nDays with temperature above 35°C:")
for day in hot_days:
    print(day)
