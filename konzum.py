import time
import sys
import requests
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


def get_page():
    # website url
    base_url = 'https://www.konzum.hr/klik/v2/'

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
            product_price = product["statistical_price"]
            all_products.append(Item(product_name, None, product_price, product_price))
            # product_weight = product["netto_weight_statement"]
            # print("\tWeight: \t", product_weight)

        # don't be rude to website owners
        time.sleep(1)

    return all_products
