import requests
from bs4 import BeautifulSoup
import pandas as pd


# TODO file naming convention (dates added to name)
# TODO go over pages (1, 2, 3 etc...)


# URL
page = requests.get("https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/")

page.status_code

# soup
soup = BeautifulSoup(page.content, 'html.parser')

offer_items = soup.find_all('div', class_="offer-wrapper")

# initiate empty lists to store all the relevant variables
links = []
titles = []
districts = []
prices = []


for offer in offer_items:

    link = offer.find('a', attrs = {'data-cy':'listing-ad-title'}, href = True)['href']
    links.append(link)

    title = offer.find('img', class_ = 'fleft')['alt']
    # title = offer.h3.strong.text
    titles.append(title)

    location_icon = offer.find('i', attrs = {'data-icon':'location-filled'})
    district_raw = location_icon.find_parent('span').text
    district = district_raw[1:].strip()
    districts.append(district)

    price_raw = offer.find('p', class_ = 'price').strong.text
    price = int(price_raw[:-2].replace(" ", ""))
    prices.append(price)


# SAVE TO CSV
results = pd.DataFrame({
    'title': titles,
    'prices': prices,
    'district': districts,
    'url_adress': links})
