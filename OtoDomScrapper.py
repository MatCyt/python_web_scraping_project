from MainScrapper import Scrapper
from bs4 import BeautifulSoup


class OtoDomScrapper(Scrapper):

    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.offer_items = self.soup.find_all('div', class_="offer-item-details")
        self.webpage_name = 'oto_dom'
        self.links = []
        self.titles = []
        self.districts = []
        self.prices = []
        self.rooms = []
        self.sqrt_mtrs = []


    def scrap_flats(self):
        # differnt approach to scrapping
        links = [a['href'] for a in self.soup.find_all('a', href = True) if a.parent.name == 'h3']
        titles = [t.get_text() for t in self.soup.find_all('span', class_="offer-item-title")]
        districts = [dist.get_text() for dist in self.soup.find_all('p', class_="text-nowrap")]
        prices = [p.get_text() for p in self.soup.find_all('li', class_="offer-item-price")]
        rooms = [r.get_text() for r in self.soup.find_all('li', class_="offer-item-rooms hidden-xs")]
        sqr_meters = [m.get_text() for m in self.soup.find_all('li', class_="hidden-xs offer-item-area")]


