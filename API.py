import os 
os.environ['SPOTIPY_CLIENT_ID'] = '72086b61b65c4865870a8dcc4d0e53a1'
os.environ['SPOTIPY_CLIENT_SECRET'] = '884050b894e14093aa8f39e419407c39'
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#returns Artist's ID through a search with name
def getArtistID(name):
    artistInfo = spotify.search(name, limit = 1, type = 'artist')
    return artistInfo['artists']['items'][0]['name']

#returns Artist's name given Artist's ID
def getArtistName(ID):
    return spotify.artist(ID)['name']

#returns Song's ID through a search with name
def getSongID(name):
    trackInfo = spotify.search(name, limit=1, type='track')
    return trackInfo['tracks']['items'][0]['id']

#returns Song's name given Song's ID
def getSongName(ID):
    return spotify.track(ID)['name']



