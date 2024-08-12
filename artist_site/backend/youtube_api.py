import time
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Requires you to enable the YouTube V3 API on your API key inside the Google Console
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/channels'

#Gets id for a specific artist using a String name
def get_youtube_channel_id(artist_name):
    params = {
        'part': 'snippet',
        'q': artist_name,
        'type': 'channel',
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    
    # Debugging: print response status code and text
    # print("YouTube search response status:", response.status_code)
    # print("YouTube search response text:", response.text)
    
    if response.status_code != 200:
        return "N/A"
    
    data = response.json()
    if 'items' not in data or not data['items']:
        return "N/A"
    
    channel_id = data['items'][0]['id']['channelId']
    return channel_id

#Gets information for a specific artist using the id from the prevoius method
def get_youtube_stats(channel_id):
    params = {
        'part': 'statistics',
        'id': channel_id,
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    
    # Debugging: print response status code and text
    # print("YouTube stats response status:", response.status_code)
    # print("YouTube stats response text:", response.text)
    
    if response.status_code != 200:
        return {
            "status": "failed to get youtube artist"
        }
    return response.json()