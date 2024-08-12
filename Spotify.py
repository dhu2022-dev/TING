import requests
import base64
import json

# Spotify API credentials
CLIENT_ID = 'b4593b81912d425d81423fcfc1d50a6a'
CLIENT_SECRET = '1803007734414e2f8f8ad098a592d51f'

# Spotify API URLs
AUTH_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = 'https://api.spotify.com/v1/search'

def get_access_token():
    """
    Get an access token from Spotify using client credentials.
    """
    auth_header = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth_header}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    
    response = requests.post(AUTH_URL, headers=headers, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    response_data = response.json()
    return response_data['access_token']

def search_artist(artist_name, access_token):
    """
    Search for an artist by name using the Spotify API.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 5  # Limit to 1 result for simplicity
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def save_to_json(data, filename):
    """
    Save data to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    # Replace with actual artist IDs or pass them as arguments
    artist_names = ['Adele', 'Taylor Swift']  # Example artist IDs

    access_token = get_access_token()

    for artist in artist_names:
        search_result = search_artist(artist, access_token)['artists']['items'][0]
        # Debugging: print the entire artist_data response
        save_to_json(search_result, 'artist_data.json')
        
        # Check for specific fields and handle missing data
        artist = search_result.get('name', 'N/A')
        genres = ', '.join(search_result.get('genres', []))
        followers = search_result.get('followers', {}).get('total', 'N/A')
        popularity = search_result.get('popularity', 'N/A')
        
        print(f"Artist Name: {artist}")
        print(f"Genres: {genres}")
        print(f"Followers: {followers}")
        print(f"Popularity: {popularity}")
        print()

if __name__ == "__main__":
    main()
