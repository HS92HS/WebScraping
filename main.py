import csv
from bs4 import BeautifulSoup
import requests

url = ('https://en.wikipedia.org/wiki/Web_scraping')
page =requests.get(url)
# print(page)
soup =BeautifulSoup(page.content,'html.parser')
# list = soup.find_all('div' class = 'mw-body ve-init-mw-desktopArticleTarget-targetContainer',)
heading = soup.find('h1',class_ = 'firstHeading mw-first-heading').text
print(heading)
description = soup.find('div', class_ = "vector-body").text
print(description)


