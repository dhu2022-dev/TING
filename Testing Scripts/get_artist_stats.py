from fastapi import FastAPI, HTTPException
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

#Requires you to enable the Youtube V3 API on your API key inside the Google Console
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/channels'

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))


class Artist(BaseModel):
    username: str


def get_youtube_channel_id(artist_name):
    params = {
        'part': 'snippet',
        'q': artist_name,
        'type': 'channel',
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    
    # Debugging: print response status code and text
    print("YouTube search response status:", response.status_code)
    print("YouTube search response text:", response.text)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching YouTube data")
    
    data = response.json()
    if 'items' not in data or not data['items']:
        raise HTTPException(status_code=404, detail="Channel not found on YouTube")
    
    channel_id = data['items'][0]['id']['channelId']
    return channel_id


def get_youtube_stats(channel_id):
    params = {
        'part': 'statistics',
        'id': channel_id,
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    
    # Debugging: print response status code and text
    print("YouTube stats response status:", response.status_code)
    print("YouTube stats response text:", response.text)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching YouTube data")
    return response.json()


def get_spotify_stats(artist_name):
    results = spotify.search(q='artist:' + artist_name, type='artist')
    if not results['artists']['items']:
        raise HTTPException(status_code=404, detail="Artist not found on Spotify")
    artist = results['artists']['items'][0]
    return artist


@app.post("/get_stats/")
def get_stats(artist: Artist):
    username = artist.username
    
    channel_id = get_youtube_channel_id(username)
    youtube_stats = get_youtube_stats(channel_id)

    spotify_stats = get_spotify_stats(username)
    
    return {
        'YouTube Stats': youtube_stats,
        'Spotify Stats': spotify_stats
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)