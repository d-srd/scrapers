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
base_url = 'https://www.konzum.hr/klik/v2/'

# read data
page = requests.get(base_url + 'categories')

# parse
parsed = page.json()

# remove the first promo page
del parsed[0]

for category in parsed:
    category_id = category["id"]
    name = category["name"]
    url = category["products_path"]
    print("ID: \t", category_id)
    print("Name: \t", name)
    print("URL: \t", url)
    print()

    products_page = requests.get(base_url + url)
    products = products_page.json()

    for product in products["products"]:
        product_id = product["id"]
        product_name = product["name"]
        product_price = product["statistical_price"]
        # product_weight = product["netto_weight_statement"]
        print("\tID: \t", product_id)
        print("\tName: \t", product_name)
        print("\tPrice: \t", product_price)
        # print("\tWeight: \t", product_weight)

    time.sleep(1)
