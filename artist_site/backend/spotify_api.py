import time
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

#Gets information for a specific artist using a String name
def get_spotify_artist_stats(artist_name):
    results = spotify.search(q='artist:' + artist_name, type='artist')
    if not results['artists']['items']:
        return "Artist Not Found"
    artist = results['artists']['items'][0]
    # print(type(artist))
    related_artists = get_related_artists(artist["id"])
    artist["related_artists"] = related_artists
    return artist

def get_related_artists(artist_id):
    similar_artists = spotify.artist_related_artists(artist_id)
    return similar_artists