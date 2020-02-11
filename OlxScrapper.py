from MainScrapper import Scrapper
from bs4 import BeautifulSoup



class OlxScrapper(Scrapper):

    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.offer_items = self.soup.find_all('div', class_="offer-wrapper")
        self.webpage_name = 'olx'
        self.links = []
        self.titles = []
        self.districts = []
        self.prices = []
        self.rooms = ''
        self.sqrt_mtrs = ''


    def scrap_flats(self):

        for offer in self.offer_items:

            link = offer.find('a', attrs = {'data-cy':'listing-ad-title'}, href = True)['href']
            self.links.append(link)

            title = offer.h3.strong.text.encode('utf=8')
            self.titles.append(title)

            location_icon = offer.find('i', attrs = {'data-icon':'location-filled'})
            district_raw = location_icon.find_parent('span').text
            district = district_raw[1:].strip().encode('utf=8', 'replace')
            self.districts.append(district)

            price_raw = offer.find('p', class_ = 'price').strong.text
            price = int(price_raw[:-2].replace(" ", ""))
            self.prices.append(price)

