#!/usr/bin/env python3

# TODO: find way to download youtube vid (50% compl); argv checking; link checking; fancy output
import sys
import re
import urllib.request
from urllib.error import URLError
from bs4 import BeautifulSoup
from pytube import Search

namelist = []
ytlist = []
playlist = sys.argv[1]

try:
    response = urllib.request.urlopen(playlist)
    html_doc = response.read()
 
 
except URLError as e:
    print("Unable to download page: "+str(e.reason))

soup = BeautifulSoup(html_doc, 'html.parser')

# Get song names

for link in soup.find_all('button'):
    if re.search("track", str(link.get('aria-label'))):
        trackname = link.get('aria-label')
        name = trackname.removeprefix('track ')
        namelist.append(name)

# Get album name
rawalbumname = soup.find_all(attrs={"property" : "og:title"})
albumname = rawalbumname[0]['content']

# Put 2 and 2 together and search youtube
for ogname in namelist:
    #print(albumname + ' ' + ogname + ' lyrics')
    s = Search(albumname + ' ' + ogname + ' lyrics')
    ytlink = s.results[0]
    print(ytlink.watch_url)
    ytlist.append(ytlink.watch_url)

#print(ytlist)

