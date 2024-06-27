import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify API endpoints
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'

# Get client ID and client secret from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Base64 encode client ID and client secret
client_credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(client_credentials.encode()).decode()

# Headers for the token request
headers = {
    'Authorization': f'Basic {encoded_credentials}'
}

# Data for the token request
data = {
    'grant_type': 'client_credentials'
}

# Make a POST request to get the access token
response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the access token from the response JSON
    access_token = response.json()['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
    print(response.text)