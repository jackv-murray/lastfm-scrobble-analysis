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
        'limit': 50,
        'from': from_timestamp,
        'to': to_timestamp,
        'format': 'json',
        'page': page
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


def get_album_info(api_key, artist, track):
    base_url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'track.getInfo',
        'artist': artist,
        'track': track,
        'api_key': api_key,
        'format': 'json'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['message']}")
        return None

    album = data['track'].get('album', {}).get('title', 'N/A')
    return album


def organize_scrobbles(scrobbles, api_key):
    timestamp_list = []
    artist_list = []
    track_list = []
    album_list = []
    top_tag_list = []

    for scrobble in scrobbles:
        timestamp = scrobble.get('date', {}).get('uts', 'N/A')
        
        if timestamp != 'N/A':
            timestamp = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        artist = scrobble['artist']['#text']
        track = scrobble['name']
        album = get_album_info(api_key, artist, track) if artist and track else 'N/A'
        tags = get_artist_top_tag(api_key, artist) if artist else 'N/A'
        

        timestamp_list.append(timestamp)
        artist_list.append(artist)
        track_list.append(track)
        album_list.append(album)
        top_tag_list.append(tags)

    return timestamp_list, artist_list, track_list, album_list, top_tag_list


def create_dataframe(timestamps, artists, tracks, albums, tags):
    data = {'Timestamp': timestamps, 'Artist': artists, 'Track': tracks, 'Album': albums, 'Top Tags': tags}
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
            break  #stops the script if it raises an error or no scrobbles left to retrieve

        all_scrobbles.extend(scrobbles)

        # Check if the number of returned scrobbles is less than the limit
        #-1 len to exclude counting header
        if len(scrobbles) < 20:
            print(f"Page {page}: {len(scrobbles) - 1} records, Time: {time.time() - start_time:.2f} seconds")
            break 


        print(f"Page {page}: {len(scrobbles) - 1} records, Time: {time.time() - start_time:.2f} seconds")
        page += 1

    if all_scrobbles:
        timestamps, artists, tracks, albums, tags = organize_scrobbles(all_scrobbles, api_key)
        df = create_dataframe(timestamps, artists, tracks, albums, tags)

        # Returns the df minus any entries with a Timestamp as 'N/A'
        # This is due to tracks being currently listened to appearing as such
        df = df[df['Timestamp'] != 'N/A']
        print(f"Total scrobbles for {yesterday.date()} is {len(df)} ") 
        return df

if __name__ == "__main__":
    result_df = main()