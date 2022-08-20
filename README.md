# sppd
# Simple Spotify playlist downloader
Download everything from your Spotify playlist/album.

## Windows
### Installation
Install Python

Open command prompt

Type `py -m pip install --user sppd`

### Running
Example:
```
py -m sppd https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```
This will download songs to your "Music" folder in webm format (cus youtube)
To change the folder, just use the -o flag.

Example:
```
py -m sppd -o ~\Donwloads https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```

## Linux
### Installation
```
sudo wget 'https://raw.githubusercontent.com/emcy06236/sppd/master/sppd.py' -O /usr/local/bin/sppd; python3 -m pip install --user pytube beautifulsoup4
```

### Running
Example:
```
sppd https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```
or
```
sppd -o ~/Downloads https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```
