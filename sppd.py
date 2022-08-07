#!/usr/bin/env python3

# TODO: find way to download youtube vid; argv checking; link checking; fancy output
import re
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError
import sys

playlist = sys.argv[1]

try:
    response = urllib.request.urlopen(playlist)
    html_doc = response.read()
 
 
except URLError as e:
    print("Unable to download page: "+str(e.reason))

soup = BeautifulSoup(html_doc, 'html.parser')

for link in soup.find_all('button'):
    if re.search("track", str(link.get('aria-label'))):
        print(link.get('aria-label'))
