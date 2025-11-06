import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

crypto_data = []

rows = soup.select('table tbody tr')

for row in rows[:10]:  # limiting to top 10 cryptos for brevity
    name = row.select_one('td:nth-child(3) p:first-child')
    symbol = row.select_one('td:nth-child(3) p:last-child')
    price = row.select_one('td:nth-child(4) a')

    if name and symbol and price:
        crypto_data.append({
            'name': name.text.strip(),
            'symbol': symbol.text.strip(),
            'price': float(price.text.replace('$', '').replace(',', '').strip())
        })

# Step 3: Display the data
print("Top Cryptocurrencies:")
for crypto in crypto_data:
    print(f"{crypto['name']} ({crypto['symbol']}): ${crypto['price']}")

# Step 4: Find and print the cryptocurrency with the highest price
if crypto_data:
    highest = crypto_data[0]
    for crypto in crypto_data:
        if crypto['price'] > highest['price']:
            highest = crypto
    print("\nHighest Priced Cryptocurrency:")
    print(f"{highest['name']} ({highest['symbol']}): ${highest['price']}")
