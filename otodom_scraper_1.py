
# TODO import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# TODO limit number of pages sent


# URL
page = requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?search%5Bfilter_float_price_per_m%3Ato%5D=8000&search%5Bfilter_float_m%3Afrom%5D=80&search%5Bdescription%5D=1&search%5Bregion_id%5D=7&search%5Bsubregion_id%5D=197&search%5Bcity_id%5D=26&search%5Border%5D=created_at_first%3Adesc&nrAdsPerPage=72&page=1")

page.status_code

# soup
soup = BeautifulSoup(page.content, 'html.parser')

offer_items = soup.find_all('div', class_="offer-item-details")

titles = soup.find_all('span', class_="offer-item-title")

soup.select()

# Linki
for a in soup.find_all('a', href = True):
    if a.parent.name == 'h3':
        print(a['href'])

# tytuł


# dzielnica


# cena


# pokoje


# m2



