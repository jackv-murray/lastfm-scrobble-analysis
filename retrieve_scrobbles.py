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
        'limit': 200,
        'from': from_timestamp,
        'to': to_timestamp,
        'format': 'json',
        'page': page
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'error' in data:
        print(f"Error: {data['message']}")
        return []

    scrobbles = data['recenttracks']['track']
    return scrobbles

def get_top_tag(api_key, artist):
    base_url = "http://ws.audioscrobbler.com/2.0/"
    params = {
        'method': 'artist.getTopTags',
        'artist': artist,
        'api_key': api_key,
        'format': 'json'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    top_tag = [tag['name'] for tag in data.get('toptags', {}).get('tag', [])]
    return top_tag

def organize_scrobbles(scrobbles, api_key):
    timestamp_list = []
    artist_list = []
    track_list = []
    album_list = []
    album_mbid_list = []
    top_tag_list = []
    mbid_list = []
    artist_mbid_list = []

    #tags are on artist-level, and take time to retrieve
    #build up a cache of artist tags for artist already captured
    top_tag_cache = {}

    for scrobble in scrobbles:
        timestamp = scrobble.get('date', {}).get('uts', 'N/A')
        artist = scrobble['artist']['#text']
        artist_mbid = scrobble['artist'].get('mbid', 'N/A')
        track_mbid = scrobble['mbid']
        track = scrobble['name']
        album = scrobble.get('album', {}).get('#text', 'N/A') 
        album_mbid = scrobble.get('album', {}).get('mbid', 'N/A') 

        #timestamps in utc format, convert to more readable form
        #current listen tracks sometimes flag as 'N/A' so below avoids error when converting N/A
        if timestamp != 'N/A':
            timestamp = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        if artist not in top_tag_cache:
            top_tag_cache[artist] = get_top_tag(api_key, artist)
        tag = top_tag_cache.get(artist)

        #append to lists which will be returned 
        timestamp_list.append(timestamp)
        artist_list.append(artist)
        track_list.append(track)
        album_list.append(album)
        album_mbid_list.append(album_mbid)
        top_tag_list.append(tag)
        mbid_list.append(track_mbid)
        artist_mbid_list.append(artist_mbid)

    return timestamp_list, artist_list, artist_mbid_list, track_list, mbid_list, album_list, album_mbid_list, top_tag_list

def create_dataframe(timestamps, artists, artist_MBID, tracks, mbids, album, album_MBID, tags):
    data = {'Timestamp': timestamps, 
            'Artist': artists, 
            'artist_MBID': artist_MBID, 
            'Track': tracks, 
            'track_MBID': mbids, 
            'Album': album, 
            'album_MBID': album_MBID,
            'Tag': tags}
    df = pd.DataFrame(data)
    return df

def main():
    
    start_total_time = time.time()
    
    
    api_key = os.getenv('API_KEY')
    username = 'sorfildor'

    #runs daily to capture previous day's scrobbles
    yesterday = datetime.now() - timedelta(days=2)
    from_timestamp = int(yesterday.replace(hour=0, minute=0, second=0, microsecond=0).timestamp())
    to_timestamp = int(yesterday.replace(hour=23, minute=59, second=59, microsecond=999999).timestamp())

    all_scrobbles = []
    page = 1

    while True:
        scrobbles = get_lastfm_scrobbles(api_key, username, from_timestamp, to_timestamp, page)
        
        if not scrobbles:
            print(f"no scrobbles for {yesterday.date()}")
            break  

        all_scrobbles.extend(scrobbles)

        #add a break clause when reach final page
        if len(scrobbles) < 200:
            print(f"page {page}: {len(scrobbles)} records")
            break 


        print(f"Page {page}: {len(scrobbles)} records")
        page += 1

    if all_scrobbles:
        timestamps, artists, artist_MBID, tracks, mbids, album, album_MBID, tags = organize_scrobbles(all_scrobbles, api_key)
        df = create_dataframe(timestamps, artists, artist_MBID, tracks, mbids, album, album_MBID, tags)

        #returns the df minus any entries with a Timestamp as 'N/A'
        #this is due to tracks being currently listened to appearing as such
        print(f"Total scrobbles for {yesterday.date()} is {len(df)}")
        end_total_time = time.time()
        print(f"Total runtime: {time.time() - start_total_time:.2f} seconds")
        return df[df['Timestamp'] != 'N/A']

if __name__ == "__main__":
    result_df = main()
    yesterday = datetime.now() - timedelta(days=2)
    file_name = yesterday.strftime("%Y-%m-%d-scrobbles.csv")
    result_df.to_csv(file_name, index=False)
