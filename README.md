# sppd
# Simple Spotify playlist downloader
Download everything from your Spotify playlist/album.

## Windows
### Installation
Install Python

Open command prompt

Type `pip install sppd`

### Running
Example:
```
sppd https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```
This will download songs to your "Music" folder in webm format (cus youtube)
To change the folder, just use the -o flag.

Example:
```
sppd -o ~\Donwloads https://open.spotify.com/album/1i4Ju3OL0Tq6QaAO2OUVdE
```

## Linux
### Installation

Python (from PyPI)
```
pip install sppd
```

Python (from git)
```
sudo wget 'https://raw.githubusercontent.com/emcy06236/sppd/master/sppd.py' -O /usr/local/bin/sppd; python3 -m pip install --user pytube beautifulsoup4
```

Bash
```
sudo wget 'https://raw.githubusercontent.com/emcy06236/sppd/master/sppd' -O /usr/local/bin/sppd
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
