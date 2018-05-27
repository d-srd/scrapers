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
print(offers)

for offer in offers:
    print(offer.tag)
