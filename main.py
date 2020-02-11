import requests
from OlxScrapper import OlxScrapper
from OtoDomScrapper import OtoDomScrapper

def main():
    olx_page = requests.get("https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/")
    otodom_page = requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/")
    OlxScrapper(olx_page).run_scrapper()
    OtoDomScrapper(otodom_page).run_scrapper()

if __name__ == '__main__':
    main()