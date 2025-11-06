import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["cryptoDB"]
collection = db["prices"]

url = "https://example.com/crypto"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cryptos = []
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) >= 3:
        name = cols[0].text.strip()
        symbol = cols[1].text.strip()
        price_text = cols[2].text.strip().replace("$", "").replace(",", "")
        try:
            price = float(price_text)
        except ValueError:
            continue
        cryptos.append({"name": name, "symbol": symbol, "price": price})

if cryptos:
    collection.insert_many(cryptos)
    print("✅ Data inserted successfully!")
else:
    print("⚠️ No cryptocurrency data found.")

top_crypto = collection.find_one(sort=[("price", -1)])
print("\n💰 Highest Priced Cryptocurrency:")
print(top_crypto)
