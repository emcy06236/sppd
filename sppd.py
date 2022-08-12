#!/usr/bin/env python3

# TODO: argv checking; link checking; fancy output; multiple downloads at same time
import sys
import os
import re
import urllib.request
from os.path import expanduser
from urllib.error import URLError
from bs4 import BeautifulSoup
from pytube import Search
from pytube import YouTube

if os.name == 'posix':
    downloadloc = os.environ.get('XDG_MUSIC_DIR', '~/Music/')
elif os.name == 'nt':
    downloadloc = expanduser("~\\Music")



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
        clean_name = re.sub('[^\w_.)( -]', '', name)
        print(clean_name)
        namelist.append(clean_name)

# Get album name
rawalbumname = soup.find_all(attrs={"property" : "og:title"})
albumname = rawalbumname[0]['content']

# Put 2 and 2 together and search youtube
for ogname in namelist:
    s = Search(albumname + ' ' + ogname)
    ytlink = s.results[0]
    print(ytlink.watch_url)
    ytlist.append(ytlink.watch_url)

# Download
for yl, nl in zip(ytlist, namelist):
    yt = YouTube(yl)
    nlfile = nl + '.webm'
    stream = yt.streams.get_by_itag(251)
    streamsize = stream.filesize / 1000000
    for_streamsize = "{:.2f}".format(streamsize)

    print('Downloading ' + '"' + nl + '"' + ' (' + str(for_streamsize) + 'MB)' + ' to ' + downloadloc)
    stream.download(output_path=downloadloc, filename=nlfile)
