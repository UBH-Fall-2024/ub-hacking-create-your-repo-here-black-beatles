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
    trackInfo = spotify.search("viva la vida", limit=1, type='track')
    return trackInfo['tracks']['items'][0]['id']

#returns Song's name given Song's ID
def getSongName(ID):
    return spotify.track(ID)['name']


