# -*- coding: utf-8 -*-

import time
import sys
import json
import requests
from bs4 import BeautifulSoup

# scrape pictures + prices of available items in Konzum

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

class Category:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __str__(self):
        return "Category named: " + self.name + " , with URL: " + self.url + " "

    def __repr__(self):
        return "Category named: " + self.name + " , with URL: " + self.url + " "


# website url
base_url = 'https://www.konzum.hr/klik/v2/categories'

# read data
page = requests.get(base_url)

# parse
parsed = json.loads(page.text)

print(json.dumps(parsed, indent=4, sort_keys=True))
