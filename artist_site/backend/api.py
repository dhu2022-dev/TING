import time
from flask import Flask, request, jsonify
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SPOTIPY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
print(SPOTIPY_CLIENT_ID)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
))

# Requires you to enable the YouTube V3 API on your API key inside the Google Console
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/channels'

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
        return "N/A"
    
    data = response.json()
    if 'items' not in data or not data['items']:
        return "N/A"
    
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
        return {
            "status": "failed to get youtube artist"
        }
    return response.json()

def get_spotify_stats(artist_name):
    results = spotify.search(q='artist:' + artist_name, type='artist')
    if not results['artists']['items']:
        return "Artist Not Found"
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

@app.route('/api/artists', methods=['GET'])
def query_page():
    artist_name = request.args.get('artist_name')
    if not artist_name:
        return jsonify({"error": "No artist name provided"}), 400
    
    artist = Artist(username=artist_name)
    stats = get_stats(artist)
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True)