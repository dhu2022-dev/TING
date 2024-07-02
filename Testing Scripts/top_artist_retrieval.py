import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_URL = 'https://api.spotify.com/v1/artists'

def get_access_token():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    client_credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(client_credentials.encode()).decode()

    headers = {
        'Authorization': f'Basic {encoded_credentials}'
    }

    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)

    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token successfully retrieved\n")
        return access_token
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        print(response.text)

def retrieve_artists():
    access_token = get_access_token()

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    params = {
        'ids': '4gzpq5DPGxSnKTe4SA8HAU,06HL4z0CvFAxyc27GXpf02,6qqNVTkY8uBg9cP3Jd7DAH,3TVXtAsR1Inumwj472S9r4,64KEffDW9EtZ1y2vBYgq8T,4r63FhuTkUYltbVAg5TQnk,246dkjvS1zLTtiykXe5h60,1Xyo4u8uXC1ZmMpatF05PJ,7dGJo4pcD2V6oG8kP0tJRR,1McMsnEElThX1knmY4oliG',  # Example artist IDs of global top artists
    }

    response = requests.get(SPOTIFY_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        top_artists = response.json()['artists']

        print("Global Top Artists:")
        for idx, artist in enumerate(top_artists, start=1):
            print(f"{idx}. {artist['name']}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        print(response.text)

if(__name__ == "__main__"):
    retrieve_artists()