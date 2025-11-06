from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

url = "https://example.com/daily-weather"

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


client = MongoClient("mongodb://localhost:27017/")
db = client["weatherDB"]
collection = db["daily_weather"]

collection.delete_many({})

collection.insert_many(weather_data)

print("\nData inserted into MongoDB successfully.")

query = {"temperature": {"$gt": 35}}
hot_days = collection.find(query)

print("\nDays with temperature above 35°C:")
for day in hot_days:
    print(day)























































































































































































































































































































































































































import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

url = "https://example.com/weather"  # change this
client = MongoClient("mongodb://localhost:27017/")
db = client["weatherDB"]
col = db["daily"]

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

data = []
for item in soup.find_all("div", class_="weather"):  # adjust tag/class
    date = item.find("span", class_="date").text
    temp = float(item.find("span", class_="temp").text.replace("°C", ""))
    cond = item.find("span", class_="cond").text
    data.append({"date": date, "temp": temp, "condition": cond})

col.insert_many(data)

for x in col.find({"temp": {"$gt": 35}}):
    print(x)
