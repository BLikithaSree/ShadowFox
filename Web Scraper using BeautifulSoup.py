import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://quotes.toscrape.com/'

# Send HTTP GET request
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all quote blocks
    quotes = soup.find_all('div', class_='quote')
    
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f'"{text}" — {author}')
else:
    print(f"Failed to retrieve page: {response.status_code}")

