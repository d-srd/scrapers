# -*- coding: utf-8 -*-

import requests
import time
import sys
from bs4 import BeautifulSoup
from array import array

# scrape pictures + prices of available items in Kaufland

class Item:
    def __init__(self, name, quantity, old_price, price):
        self.name = name
        self.quantity = quantity
        self.old_price = old_price
        self.price = price

    def __str__(self):
        return "Name: " + self.name + \
            "\nQuantity: " + self.quantity + \
            "\nOld price: " + self.old_price + \
            "\nPrice: " + self.price

    def __repr__(self):
        return __str__(self)

    def get_discount_level(self):
        return self.price / self.old_price


# website url
rand_url = 'https://www.kaufland.hr/ponuda/ponuda-pregled.category=02_Svježa_riba.html'
base_url = 'https://www.kaufland.hr/'

# request
req = requests.get(rand_url, headers={'User-Agent': 'Mozilla Firefox'})
content = req.content

# parsed html
soup = BeautifulSoup(content, 'html.parser')

# get categories container, map to list of categories URLs
categories_outer = soup.find('div', attrs={'id': 'offers-overview-1'})
categories_elements = categories_outer.find_all('a', href=True)
categories = []

for element in categories_elements:
    categories.append(element['href'])
    print("Kategorija: ", element['href'])

# get all items in category
for category in categories:
    r = requests.get(base_url + category, headers={'User-Agent': 'Mozilla Firefox'})
    c = r.content
    page = BeautifulSoup(c, 'html.parser')

    # remove currency tags for easier parsing
    for span in page.find_all('span', attrs={'class': 'a-pricetag__currency'}):
        span.decompose()

    offers = page.find_all('div', attrs={'class': 'm-offer-tile'})
    items = []

    for offer in offers:
        title = offer.find('h4', attrs={'class': 'm-offer-tile__title'})
        # sometimes the subtitle is used as the actual title. this is a hack.
        if title is None:
            title = offer.find('h5', attrs={'class': 'm-offer-tile__subtitle'})
        title = title.string.strip()
        quantity = offer.find('div', attrs={'class': 'm-offer-tile__quantity'}).string.strip()
        old_price = offer.find('div', attrs={'class': 'a-pricetag__old-price'}).string.strip()
        price = offer.find('div', attrs={'class': 'a-pricetag__price'}).text.strip()
        items.append(Item(title, quantity, old_price, price))

    # test that it works
    print('[%s]' % ', '.join(map(str, items)))

    # don't be rude to website owners
    time.sleep(1)
