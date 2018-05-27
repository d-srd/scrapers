# -*- coding: utf-8 -*-

import requests
import time
import sys
from bs4 import BeautifulSoup
from array import array

# scrape pictures + prices of available items in Interspar

class Item:
    def __init__(self, name, quantity, old_price, price):
        self.name = name
        self.quantity = quantity
        self.old_price = old_price
        self.price = price

    def __str__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + self.quantity + \
            "\nOld price: " + self.old_price + \
            "\nPrice: " + self.price

    def __repr__(self):
        return "\nName: " + self.name + \
            "\nQuantity: " + self.quantity + \
            "\nOld price: " + self.old_price + \
            "\nPrice: " + self.price

    def get_discount_level(self):
        return self.price / self.old_price


# website url
base_url = 'https://www.spar.hr/hr_HR/aktualno-za-kupce-hr/1.html'

# request
req = requests.get(base_url, headers={'User-Agent': 'Mozilla Firefox'})
content = req.content

# parsed html
soup = BeautifulSoup(content, 'html.parser')


# get all items in category
req = requests.get(base_url, headers={'User-Agent': 'Mozilla Firefox'})
content = req.content
page = BeautifulSoup(content, 'html.parser')

# remove all currency symbols for easier parsing
for currency_symbol in page.find_all('span', attrs={'class': 'currency-aspiag'}):
    currency_symbol.decompose()

offers = page.find_all('div', attrs={'class': 'modul-small aktionsmodule socialMediaStart'})
offers.pop(0)
items = []

def insert_separator(currency_string):
    return currency_string[:2] + ',' + currency_string[2:]

for offer in offers:
    title = offer.find('div', attrs={'class': 'rich-text'})
    title = title.find('h3')
    title = title.find('a')
    title = title.find('div', attrs={'class': 'wrapper'})
    title = title.text.strip()
    quantity = offer.find('div', attrs={'class': 'preis-info-aspiag'})
    quantity = quantity.find('p', attrs={'info'})
    quantity = quantity.text.strip()
    price = offer.find('div', attrs={'class': 'buble-preis-aspiag'})
    old_price = price.find('p', attrs={'class': 'discount strikethrough'})
    old_price = old_price.text.strip()
    old_price = insert_separator(old_price)
    price = price.find('p', attrs={'action-preises'})
    price = price.text.strip()
    price = insert_separator(price)
    print("Title: ", title)
    print("Quantity: ", quantity)
    print("Price: ", price)
    print("Old price: ", old_price)

# test that it works
# print('[%s]' % ', '.join(map(str, items)))
