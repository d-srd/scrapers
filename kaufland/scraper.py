# -*- coding: utf-8 -*-

import requests
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
            "Quantity: " + self.quantity + \
            "Old price: " + self.old_price + \
            "Price: " + self.price

    def __repr__(self):
        return __str__(self)

    def get_discount_level(self):
        return self.price / self.old_price

# website url
fish_page = 'https://www.kaufland.hr/ponuda/ponuda-pregled.category=02_Svježa_riba.html'

# request
req = requests.get(fish_page, headers={'User-Agent': 'Mozilla Firefox'})
content = req.content

# parsed html
page = BeautifulSoup(content, 'html.parser')

# remove currency tags for easier parsing
for span in page.find_all('span', attrs={'class': 'a-pricetag__currency'}):
    span.decompose()

offers = page.find_all('div', attrs={'class': 'm-offer-tile'})
items = []

for offer in offers:
    title = offer.find('h4', attrs={'class': 'm-offer-tile__title'}).string.strip()
    quantity = offer.find('div', attrs={'class': 'm-offer-tile__quantity'}).string.strip()
    old_price = offer.find('div', attrs={'class': 'a-pricetag__old-price'}).string.strip()
    price = offer.find('div', attrs={'class': 'a-pricetag__price'}).text.strip()
    items.append(Item(title, quantity, old_price, price))

print('[%s]' % ', '.join(map(str, items)))
