import requests

def fetch_artist_stats(artist_name):
    url = 'http://localhost:5000/api/artists'
    params = {'artist_name': artist_name}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch artist stats. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    artist_name = input("Enter the artist name: ")
    stats = fetch_artist_stats(artist_name)
    
    if stats:
        print("Spotify Stats:")
        print(stats['Spotify Stats'])
        
        print("\nYouTube Stats:")
        print(stats['YouTube Stats'])