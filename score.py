# -*- coding: utf-8 -*-

from lxml import html
import requests
import sys

headers = { 'User-Agent': 'needed' }
recent = len(sys.argv)

if recent > 1:
    url = 'http://www.metacritic.com/g00/browse/games/score/metascore/90day/ps4/filtered'
else:
    url = 'http://www.metacritic.com/g00/browse/games/score/metascore/all/ps4/filtered'

page = requests.get(url, headers=headers)

tree = html.fromstring(page.content)

titles_arr = tree.xpath("//div[contains(@class, 'product_row game')]/div[contains(@class, 'product_item product_title')]/a/text()")
rating_arr = tree.xpath("//div[contains(@class, 'product_row game')]/div[contains(@class, 'product_item product_userscore_txt')]/span[contains(@class, 'data textscore')]/text()")
combined_arr = []

for idx, val in enumerate(titles_arr):
    combined_arr.append([val, rating_arr[idx]])

sorted_arr = sorted(combined_arr, key=lambda x: x[1], reverse=True)

for idx, val in enumerate(sorted_arr):
    if not val[1] == "tbd":
        print("%s || Userscore: %s \n" % (val[0].strip(), val[1].strip()))
