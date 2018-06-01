import time
import sys
import requests
import re
import os.path
import sqlite3
from bs4 import BeautifulSoup
from item import Item

# scrape pictures + prices of available items in Konzum

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

def get_page():
    # read data
    page = requests.get(base_url + 'categories')
    parsed = page.json()

    # remove the first promo page
    del parsed[0]

    return parsed

def get_products():
    page = get_page()
    all_products = []

    for category in page:
        category_id = category["id"]
        name = category["name"]
        url = category["products_path"]

        products_page = requests.get(base_url + url)
        products = products_page.json()

        for product in products["products"]:
            product_id = product["id"]
            product_name = product["name"]
            product_price = str(product["price"]["amount"])
            product_price = product_price[:-2] + '.' + product_price[-2:]
            product_price = float(product_price)
            all_products.append(Item(product_name, 1, product_price, 0))
            # product_weight = product["netto_weight_statement"]
            # print("\tWeight: \t", product_weight)

        # don't be rude to website owners
        time.sleep(0.5)

    return all_products

def save_to_db(name, items):

    conn = sqlite3.connect(name)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (name text, quantity int, price real, discount_factor real)''')

    for item in items:
        c.execute('''INSERT INTO products VALUES (?, ?, ?, ?)''', (item.name, item.quantity, item.price, item.discount_factor))

    conn.commit()

    conn.close()

products = get_products()
print('[%s]' % ', '.join(map(str, products)))
save_to_db('konzum.db', products)
