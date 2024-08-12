import time
from flask import Flask, request, jsonify
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv
import spotify_api
import youtube_api


load_dotenv()

app = Flask(__name__)

class Artist(BaseModel):
    username: str

@app.post("/get_stats/")
def get_stats(artist: Artist):
    username = artist.username
    
    channel_id = youtube_api.get_youtube_channel_id(username)
    youtube_stats = youtube_api.get_youtube_stats(channel_id)

    spotify_stats = spotify_api.get_spotify_artist_stats(username)
    print(type(youtube_stats), type(spotify_stats))
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