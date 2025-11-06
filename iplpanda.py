import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/Indian_Premier_League"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers)

tables = pd.read_html(response.text)
print(tables[2])
ipl_teams = tables[2]

print("Original IPL Teams Table:\n")
print(ipl_teams.head())


# Convert the 'Founded' column to numeric (in case it's stored as string)
ipl_teams['Founded'] = pd.to_numeric(ipl_teams['Founded'], errors='coerce')

# a. Filter teams founded in or after 2010
filtered_teams = ipl_teams[ipl_teams['Founded'] >= 2010]

# b. Sort alphabetically by Team name
sorted_teams = filtered_teams.sort_values(by='Team')

print("\nFiltered and Sorted IPL Teams (Founded after 2010):\n")
print(sorted_teams)
