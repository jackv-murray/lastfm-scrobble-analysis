from datetime import date, datetime, timedelta
import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



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

@transformer
def transform(data, *args, **kwargs):

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

    for scrobble in data:
        timestamp = scrobble.get('date', {}).get('uts', 'N/A')
        artist = scrobble['artist']['#text']
        artist_mbid = scrobble['artist'].get('mbid', 'N/A')
        track_mbid = scrobble['mbid']
        track = scrobble['name']
        album = scrobble.get('album', {}).get('#text', 'N/A') 
        album_mbid = scrobble.get('album', {}).get('mbid', 'N/A') 
        tags = scrobble.get('top_tag', [])

        #timestamps in utc format, convert to more readable form
        #current listen tracks sometimes flag as 'N/A' so below avoids error when converting N/A
        if timestamp != 'N/A':
            timestamp = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        #to handle tags in array format
        merged_tags = ', '.join(tags)


        #append to lists which will be returned 
        timestamp_list.append(timestamp)
        artist_list.append(artist)
        track_list.append(track)
        album_list.append(album)
        album_mbid_list.append(album_mbid)
        top_tag_list.append(merged_tags)
        mbid_list.append(track_mbid)
        artist_mbid_list.append(artist_mbid)


    df = create_dataframe(timestamp_list, artist_list, artist_mbid_list, track_list, mbid_list, album_list, album_mbid_list, top_tag_list)
    return df[df['Timestamp'] != 'N/A']


