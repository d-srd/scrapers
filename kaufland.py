# -*- coding: utf-8 -*-

import requests
import time
import sys
from bs4 import BeautifulSoup
from array import array

# scrape pictures + prices of available items in Kaufland

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
    rand_url = 'https://www.kaufland.hr/ponuda/ponuda-pregled.category=02_Svježa_riba.html'
    base_url = 'https://www.kaufland.hr/'

    # request
    req = requests.get(rand_url, headers={'User-Agent': 'Mozilla Firefox'})
    content = req.content

    # parsed html
    soup = BeautifulSoup(content, 'html.parser')

    return soup

def get_categories():
    soup = get_page()

    # get categories container, map to list of categories URLs
    categories_outer = soup.find('div', attrs={'id': 'offers-overview-1'})
    categories_elements = categories_outer.find_all('a')
    categories = []

    for element in categories_elements:
        categories.append(Category(element['href'], element.text.strip()))
        print("Kategorija: ", element.text.strip())

    return categories

def get_products():
    categories = get_categories()
    items = []

    # get all items in category
    for category in categories:
        r = requests.get(base_url + category.url, headers={'User-Agent': 'Mozilla Firefox'})
        c = r.content
        page = BeautifulSoup(c, 'html.parser')

        # remove currency tags for easier parsing
        for span in page.find_all('span', attrs={'class': 'a-pricetag__currency'}):
            span.decompose()

        offers = page.find_all('div', attrs={'class': 'm-offer-tile'})

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
        # print('[%s]' % ', '.join(map(str, items)))

        # don't be rude to website owners
        time.sleep(1)

    return items
