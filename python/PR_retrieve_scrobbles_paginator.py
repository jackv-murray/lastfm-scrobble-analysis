import requests
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
import pandas as pd
import time

load_dotenv()

def get_lastfm_scrobbles(api_key, username, from_timestamp, to_timestamp, page=1):
    base_url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'user.getrecenttracks',
        'user': username,
        'api_key': api_key,
        'limit': 20,
        'from': from_timestamp,
        'to': to_timestamp,
        'format': 'json',
        'page': page  # Add the page parameter
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['message']}")
        return None

    scrobbles = data['recenttracks']['track']
    return scrobbles


def get_artist_top_tag(api_key, artist):
    base_url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'artist.getTopTags',
        'artist': artist,
        'api_key': api_key,
        'format': 'json'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['message']}")
        return None

    tags = [tag['name'] for tag in data.get('toptags', {}).get('tag', [])]
    top_tag = tags[0] if tags else 'N/A'
    return top_tag


def organize_scrobbles(scrobbles, api_key):
    timestamp_list = []
    artist_list = []
    track_list = []
    top_tag_list = []

    for scrobble in scrobbles:
        timestamp = scrobble.get('date', {}).get('uts', 'N/A')
        
        if timestamp != 'N/A':
            timestamp = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        artist = scrobble['artist']['#text']
        track = scrobble['name']
        tags = get_artist_top_tag(api_key, artist) if artist else None
        

        timestamp_list.append(timestamp)
        artist_list.append(artist)
        track_list.append(track)
        top_tag_list.append(tags)

    return timestamp_list, artist_list, track_list, top_tag_list


def create_dataframe(timestamps, artists, tracks, tags):
    data = {'Timestamp': timestamps, 'Artist': artists, 'Track': tracks, 'Top Tags': tags}
    df = pd.DataFrame(data)
    return df


def main():
    api_key = os.getenv('API_KEY')
    username = 'sorfildor'

    # Get timestamps for the previous day
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    from_timestamp = int(yesterday.replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    to_timestamp = int(yesterday.replace(hour=23, minute=59, second=59, microsecond=999999).timestamp())

    all_scrobbles = []
    page = 1

    while True:
        start_time = time.time()
        scrobbles = get_lastfm_scrobbles(api_key, username, from_timestamp, to_timestamp, page)
        
        if not scrobbles:
            break  # No more pages or an error occurred

        all_scrobbles.extend(scrobbles)

        # Check if the number of returned scrobbles is less than the limit
        if len(scrobbles) < 20:
            print(f"Page {page}: {len(scrobbles)} records, Time: {time.time() - start_time:.2f} seconds")
            break 


        print(f"Page {page}: {len(scrobbles)} records, Time: {time.time() - start_time:.2f} seconds")
        page += 1

    if all_scrobbles:
        timestamps, artists, tracks, tags = organize_scrobbles(all_scrobbles, api_key)
        df = create_dataframe(timestamps, artists, tracks, tags)

        # Returns the df minus any entries with a Timestamp as 'N/A'
        # This is due to tracks being currently listened to appearing as such
        print(f"Total scrobbles for {yesterday.date()} is {len(df)}")
        return df[df['Timestamp'] != 'N/A']

if __name__ == "__main__":
    result_df = main()