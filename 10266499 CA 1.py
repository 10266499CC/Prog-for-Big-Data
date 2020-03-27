# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# This a list of all of the Oscar winning movies, from 1927 to 2019 inclusive.  
# It was taken from https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films

# Converted the cURL command to python code using https://curl.trillworks.com/
# The code below contains the python code from https://curl.trillworks.com/

import requests

headers = {
    'authority': 'en.wikipedia.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'WMF-Last-Access=27-Mar-2020; WMF-Last-Access-Global=27-Mar-2020; GeoIP=IE:L:Athlone:53.42:-7.94:v4; enwikimwuser-sessionId=1ecc224ef612e566c51c',
    'if-modified-since': 'Tue, 17 Mar 2020 01:16:16 GMT',
}

response = requests.get('https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films', headers=headers)

# Printed out the contents to the screen 

print(response.content)

# Consulted https://www.crummy.com/software/BeautifulSoup/bs4/doc/ to retrieve the Beautiful Soup code. 

# Imported Beautiful Soup

from bs4 import BeautifulSoup

# Changed the response.content to a Beautiful Soup Object

soup = BeautifulSoup(response.content, 'html.parser')

# Beautiful Soup formatted the html nicely

print(soup.prettify())

