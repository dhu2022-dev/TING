import requests
import json

# Define API key and base URLs
API_KEY = 'PKgRHvbfYjxWr7qkOFplRgvBGCFO5ewo'
SEARCH_URL = 'https://app.ticketmaster.com/discovery/v2/events.json'
EVENT_URL = 'https://app.ticketmaster.com/discovery/v2/events/'

def search_adele_concerts(num_events=1):
    """
    Search for Adele concerts using the Discovery API.
    
    :param num_events: Number of recent events to retrieve.
    :return: List of event dictionaries.
    """
    params = {
        'apikey': API_KEY,
        'keyword': 'Adele',
        'sort': 'date,desc',  # Sort by date in descending order to get the most recent events
        'size': num_events    # Number of events to retrieve
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    # Extract the list of events
    events = data.get('_embedded', {}).get('events', [])
    return events

def get_event_sales(event_id):
    """
    Get sales information for a specific event.
    
    :param event_id: The ID of the event.
    :return: Event details including sales information.
    """
    url = f'{EVENT_URL}{event_id}.json'
    params = {
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def save_to_json(data, filename):
    """
    Save data to a JSON file.
    
    :param data: Data to be saved.
    :param filename: Name of the file to save data to.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    num_events = 5  # Set the number of recent events you want to retrieve
    # Find the latest Adele concerts
    events = search_adele_concerts(num_events=num_events)
    
    if events:
        # Get details for each event and save to JSON
        events_details = []
        for event in events:
            event_id = event.get('id')
            if event_id:
                event_data = get_event_sales(event_id)
                events_details.append(event_data)
        
        # Save the events details to a JSON file
        save_to_json(events_details, 'adele_concerts.json')
        print(f"Saved {num_events} events to 'adele_concerts.json'.")
    else:
        print("Failed to find Adele concerts.")

if __name__ == "__main__":
    main()
