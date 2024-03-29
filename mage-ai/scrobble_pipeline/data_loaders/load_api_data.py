import io
import pandas as pd
from datetime import date, datetime, timedelta
from mage_ai.data_preparation.shared.secrets import get_secret_value
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def data_loader(**kwargs):

    base_url = "http://ws.audioscrobbler.com/2.0/"
    page = 1
    all_scrobbles = []
    yesterday = datetime.now() - timedelta(days=1)

    while True:
        recent_tracks_params = {
            'method': 'user.getrecenttracks',
            'user': (kwargs.get('username')),
            'api_key': get_secret_value('API_KEY'),
            'limit': 200,
            'from': int(yesterday.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()),
            'to': int(yesterday.replace(hour=23, minute=59, second=59, microsecond=999999).timestamp()),
            'format': 'json',
            'page': page
        }

        recent_tracks_response = requests.get(base_url, params=recent_tracks_params)
        recent_tracks_data = recent_tracks_response.json()

        if 'error' in recent_tracks_data:
            print(f"Error: {recent_tracks_data['message']}")
            return []

        scrobbles = recent_tracks_data['recenttracks']['track']

        # Get top tag for each artist
        scrobbles_with_tags = []
        for track in scrobbles:
            artist = track.get('artist', {}).get('#text', '')
            if artist:
                top_tag_params = {
                    'method': 'artist.getTopTags',
                    'artist': artist,
                    'api_key': get_secret_value('API_KEY'),
                    'format': 'json'
                }
                top_tag_response = requests.get(base_url, params=top_tag_params)
                top_tag_data = top_tag_response.json()
                top_tag = [tag['name'] for tag in top_tag_data.get('toptags', {}).get('tag', [])]
                track['top_tag'] = top_tag
            scrobbles_with_tags.append(track)

        all_scrobbles.extend(scrobbles_with_tags)

        if len(scrobbles) < 200:
            break

        page += 1

    
    return all_scrobbles


