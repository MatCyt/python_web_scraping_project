import requests

# send get request
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# check the status code - 2## success, 4## / 5## failure
page.status_code

# content - a html document
page.content



# BeautifulSoup to read through html documents
from bs4 import BeautifulSoup

# create a BS class to parse document
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# manual navigation over parent children
test1 = list(soup.children)[2]
test2 = list(test1.children)[3]
test3 = list(test2.children)[1]
test3.get_text()

# find_all - tags 
soup.find_all('p')
soup.find_all('p')[0].get_text()


# search for tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
soup

# find all to look for classes or ids
soup.find_all(class_="outer-text")

soup.find_all(id = 'first')

# search over css selectors
# search for all p tags inside div
soup.select("div p")


# DOWNLOAD PAGE
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XhhM68hKgnI')
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id = 'seven-day-forecast')
forecast_items = seven_day.find_all(class_ = 'tombstone-container')

# extract information for tonight
tonight = forecast_items[0]

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)


# extract all at once
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

# store into csv
import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
weather
