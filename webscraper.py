from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(page):
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
