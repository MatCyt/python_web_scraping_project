import os
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


class Scrapper():

    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.offer_items = ''
        self.webpage_name = ''
        self.links = []
        self.titles = []
        self.districts = []
        self.prices = []
        self.rooms = []
        self.sqrt_mtrs = []


    def scrap_flats(self):
        pass


    def generate_file_name(self):
        current_date = date.today().strftime('%d-%m-%Y')
        filename = self.webpage_name + '_' + current_date + '.csv'

        this_folder = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.join(this_folder, filename)
        return path_file


    def save_results(self):
        results = pd.DataFrame({
        'title': self.titles,
        'price': self.prices,
        'district': self.districts,
        'rooms': self.rooms,
        'sqrt_mtrs': self.sqrt_mtrs,
        'url_adress': self.links})

        path_file = self.generate_file_name()

        results.to_csv(path_file)


    def run_scrapper(self):
        self.scrap_flats()
        self.save_results()
