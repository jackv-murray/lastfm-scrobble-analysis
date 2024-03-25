<p align="center">
<picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/section%203.png" width="800">
</picture>
</p>

The last.fm API adheres to RESTful principles, in which we make HTTP requests to call methods such as .get and receive responses in JSON format. Further information can be found [here](https://www.last.fm/api/intro). 

The data is extracted from the API using the [user.getRecentTracks](https://www.last.fm/api/show/user.getRecentTracks) method. This will retrieve a record of scrobbling data for a specified user across a specified timeframe,
along with associated metadata for the track such as artist and album name and IDs. The [artist.getTopTags](https://www.last.fm/api/show/artist.getTopTags) method is also used to attach genre tags for each artist.

The API has been around for a long time. Here's a tutorial provided by [dataquest.io](https://www.dataquest.io/blog/last-fm-api-python/) which serves as a good starting point. 

## API Key

You'll require a [key](https://www.last.fm/api/account/create) in order to interact with the API. Follow the instructions and make note of your API Key. 

##
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/back.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/infrastructure_deployment.md)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/next.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
