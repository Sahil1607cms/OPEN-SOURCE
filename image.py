import requests
from bs4 import BeautifulSoup

url = input("Enter the webpage URL: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url,headers=headers)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, 'html.parser')

    images = soup.find_all('img')

    print(f"\nFound {len(images)} image(s):\n")
    for i, img in enumerate(images, start=1):
        src = img.get('src')
        if src:
            print(f"{i}. {src}")
        else:
            print(f"{i}. [No src attribute found]")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
