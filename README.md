<p align="center">
 <picture>
 <img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/main%20heading.png" width="800">
 </picture>
 </p>

In this data engineering project, I develop an end-to-end solution to analyse my listening history by building a pipeline to extract my scrobbles from the last.fm API, process and model the data before finally visualising the results in a Tableau dashboard.

This is a batch pipeline scheduled to run each day by extracting the previous day's scrobbles and loading them into Google Cloud Storage, to be processed further on. The pipeline can also be configured to capture scrobbles between specified date points, such as to retrieve the last few years worth of data. This then feeds into a Tableau dashboard, which aims to provide some insight into my listening habits.  Docs for the API can be found here: [:musical_note:](https://www.last.fm/api/intro)


<h1 align="center">What is last.fm?</h1>
A website which records your listening history, with integrations into Spotify, Deezer etc. I've had an account for a very long time, so it was great to use that historic data in a project. Please support them by making an account and syncing it with your streaming app of choice.

<h2 align="center"> last.fm 'scrobbles'</h2>
A scrobble is a record of what you listened to, on an individual track level, so each scrobble equals one track played. In addition to the name of the track, each scrobble also contains information about the time you listened to it, name of the artist and album, genre and so on. 
<br />
<br />
<br />
<p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/project%20objectives.png" width="800">
 </picture>
 </p>                               
 After the data has been extracted from the Last.fm API, I aim to model the data in accordance with star schema principles. This involves organising the data into fact and dimension tables to facilitate efficient analysis and querying. 
 For the analysis part, I will create a Tableau dashboard and aim to answer the following questions:
<br /> <br />

 * What sort of genres do I listen to the most?
 * At what time of the day do I listen to the most music?
 * Has my listening preferences changed over the years?
 * How many tracks do I listen to on average per day?



<h2 align="center">Data set</h2>

The data is extracted from the last.fm API, which is essentially the same listening data held on my last.fm profile. I use the user.getrecenttracks and artist.gettoptags methods, retrieving a record of my scrobbling history including: timestamps, artist, album, track, associated MusicBrainz IDs and artist genre tags.

<br />
<p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/project%20architecture.png" width="800">
 </picture>
 </p>
 
<p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/project%20overview.png" width="800">
 </picture>
 </p>



<p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm-scrobble-analysis/assets/102922713/b240be9c-34b2-4033-b122-bfcfa545efb4" width="50">
 </picture>
 </p>


[![project](https://github.com/jackv-murray/lastfm-scrobble-analysis/blob/main/assets/scrobble_db.png)](https://public.tableau.com/app/profile/jack.murray5825/viz/Last_fm-ScrobbleInsights/design2)


</br>

 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/reproducibility.png" width="800">
 </picture>
 </p>



To follow-along and run the pipeline in your own environment, please see the below sections. You may need to adjust some of the instructions if you're not running it on a Linux machine.  

[Section 1 - Environment Set-up](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/environment_setup.md)

[Section 2 - Infrastructure deployment](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/infrastructure_deployment.md)

[Section 3 - last.fm API](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/lastfm_api.md)

[Section 4 - Mage Orchestration](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/mage_orchestration.md)

[Section 5 - Modelling with dbt](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/modelling_with_dbt.md)

[Section 6 - Data Visualisation](https://github.com/jackv-murray/lastfm-scrobble-analysis/blob/main/reproducibility/data_visualisation.md)

[Thoughts and improvements](https://github.com/jackv-murray/lastfm-scrobble-analysis/blob/main/reproducibility/thoughts_and_improvements.md)

