import pandas as pd
from bs4 import BeautifulSoup
import requests

url ="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')

tables = pd.read_html(url)
print(f"Found {len(tables)} tables")
print(tables[0].head())