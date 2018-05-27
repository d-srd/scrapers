# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# scrape pictures + prices of available items in Kaufland

# website url
fish_page = 'https://www.kaufland.hr/ponuda/ponuda-pregled.category=02_Svježa_riba.html'

# request
req = requests.get(fish_page, headers={'User-Agent': 'Mozilla Firefox'})
content = req.content

# parsed html
page = BeautifulSoup(content, 'html.parser')

offers = page.find_all('div', attrs={'class': 'm-offer-tile'})

for offer in offers:
    title = offer.find('h4', attrs={'class': 'm-offer-tile__title'})
    quantity = offer.find('div', attrs={'class': 'm-offer-tile__quantity'})
    old_price = offer.find('div', attrs={'class': 'a-pricetag__old-price'})
    price = offer.find('div', attrs={'class': 'a-pricetag__price'})
    print(title, quantity, old_price, price)
