# -*- coding: utf-8 -*-

from lxml import html
import requests

headers = { 'User-Agent': 'needed' }
platforms = "all ps4 xboxone switch pc wii-u 3ds vita ios"
platform = raw_input("What platform do you want to display? Possible options: {}\n".format(platforms))

if platform not in platforms:
    print("You mistyped the platform or it is not supported..")
    quit()
else:
    time = raw_input("Limit score to last 90days? y/n \n")

    if time == "y":
        time = "90day"
    else:
        time = "all"
    url = 'http://www.metacritic.com/g00/browse/games/score/metascore/{}/{}/filtered'.format(time, platform)

page = requests.get(url, headers=headers)

tree = html.fromstring(page.content)

titles_arr = tree.xpath("//div[contains(@class, 'product_row game')]/div[contains(@class, 'product_item product_title')]/a/text()")
rating_arr = tree.xpath("//div[contains(@class, 'product_row game')]/div[contains(@class, 'product_item product_userscore_txt')]/span[contains(@class, 'data textscore')]/text()")
combined_arr = []

for idx, val in enumerate(titles_arr):
    if not rating_arr[idx] == "tbd":
        combined_arr.append([val, rating_arr[idx]])

sorted_arr = sorted(combined_arr, key=lambda x: x[1], reverse=True)

for idx, val in enumerate(sorted_arr):
    print("Platz %s || %s || Userscore: %s \n" % (idx + 1, val[0].strip(), val[1].strip()))
