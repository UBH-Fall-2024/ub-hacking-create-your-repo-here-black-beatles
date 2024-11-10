import os 
os.environ['SPOTIPY_CLIENT_ID'] = '72086b61b65c4865870a8dcc4d0e53a1'
os.environ['SPOTIPY_CLIENT_SECRET'] = '884050b894e14093aa8f39e419407c39'
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

#returns Artist's ID through a search with name
def search(name):
    artistList = []
    songList = []
    info = spotify.search(name, limit = 3, type ='artist,track')
    for i in range(3):
        songList.append(info['tracks']['items'][i]['id'])
    for i in range(3):
        artistList.append(info['artists']['items'][i]['id'])
    artistList.extend(songList)
    return artistList

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


def getArtistData(ID):
    info = {
        
    }
    artistInfo = spotify.artist(ID)
    info.update({'followers': artistInfo['followers']['total']})
    info.update({'image': artistInfo['images'][0]['url']})
    info.update({'artistName': artistInfo['name']})
    artistInfo = spotify.artist_top_tracks(ID)
    i = 0
    while i < 3 and i < len(artistInfo['tracks']):
        info.update({f'song{i+1}Name': artistInfo['tracks'][i]['name']})
        i += 1
    return info

def getSongData(ID):
    info = {

    }
    songInfo = spotify.track(ID)
    info.update({'album' : songInfo['album']['name']})
    info.update({'release_date' : songInfo['album']['release_date']})
    info.update({'image' : songInfo['album']['images'][0]['url']})
    info.update({'name' : songInfo['album']['name']})
    return info
