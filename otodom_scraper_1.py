
import requests
from bs4 import BeautifulSoup
import pandas as pd



# TODO split lines in districts
# TODO polish letters encoding przykladowy_string.encode("utf-8")
# TODO leave only float in sqr metters
# TODO prices
# TODO scrap multiple pages (set all pages to be scrapped? data, last sent?)



# URL
page = requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?search%5Bfilter_float_price_per_m%3Ato%5D=8000&search%5Bfilter_float_m%3Afrom%5D=80&search%5Bdescription%5D=1&search%5Bregion_id%5D=7&search%5Bsubregion_id%5D=197&search%5Bcity_id%5D=26&search%5Border%5D=created_at_first%3Adesc&nrAdsPerPage=72&page=1")

page.status_code

# soup
soup = BeautifulSoup(page.content, 'html.parser')

offer_items = soup.find_all('div', class_="offer-item-details")


# Links
links = [a['href'] for a in soup.find_all('a', href = True) if a.parent.name == 'h3']

# titles
titles = [t.get_text() for t in soup.find_all('span', class_="offer-item-title")]

# dzielnica
districts = [dist.get_text() for dist in soup.find_all('p', class_="text-nowrap")]

# cena
prices = [p.get_text() for p in soup.find_all('li', class_="offer-item-price")]

# pokoje
rooms = [r.get_text() for r in soup.find_all('li', class_="offer-item-rooms hidden-xs")]

# m2
sqr_meters = [m.get_text() for m in soup.find_all('li', class_="hidden-xs offer-item-area")]

# save to csv
results = pd.DataFrame({
    'title': titles,
    'prices': prices,
    'district': districts,
    'rooms': rooms,
    'sqr_meters': sqr_meters,
    'url_adress': links})


results.to_csv('oto_dom_scrap.csv')