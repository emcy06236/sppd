#!/usr/bin/env python3

# TODO: link checking; fancy output; multiple downloads at same time
import sys
import os
import argparse
import re
import urllib.request
from os.path import expanduser
from urllib.error import URLError
from bs4 import BeautifulSoup
from pytube import Search
from pytube import YouTube

if os.name == 'posix':
    rawdownloadloc = os.environ.get('XDG_MUSIC_DIR', '~/Music/')
elif os.name == 'nt':
    rawdownloadloc = '~\\Music'

parser = argparse.ArgumentParser(description='Download Spotify playlist songs from YouTube')
parser.add_argument('-o', '--output', help='Specify download directory')
parser.add_argument('PLAYLIST', type=str)
args = parser.parse_args()

playlist = args.PLAYLIST
if args.output != None:
    rawdownloadloc = args.output
downloadloc = expanduser(str(rawdownloadloc))

namelist = []
ytlist = []


try:
    response = urllib.request.urlopen(playlist)
    html_doc = response.read()
 
 
except URLError as e:
    print("Unable to download page: "+str(e.reason))

print("Downloading Webpage")
soup = BeautifulSoup(html_doc, 'html.parser')

print("Finding album name")
# Get album name
rawalbumname = soup.find_all(attrs={"property" : "og:title"})
if len(rawalbumname) == 0:
    print("Couldn't find album name, check playlist in browser or report bug")
    sys.exit(1)

albumname = rawalbumname[0]['content']

print("Finding song names")
# Get song names
for link in soup.find_all('div'):
    if not re.search("None", str(link.get('aria-label'))):
        trackname = link.get('aria-label')
        clean_name = re.sub('[^\w_.)( -]', '', trackname)
        namelist.append(clean_name)

print("Searching YouTube, this will take a while")
# Put 2 and 2 together and search youtube
for ogname in namelist:
    s = Search(albumname + ' ' + ogname + ' explicit')
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
