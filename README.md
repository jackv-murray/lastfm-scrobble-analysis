# [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Lastfm_logo.svg/2560px-Lastfm_logo.svg.png" width="80">](https://last.fm) scrobble analysis 

**replace logos with copies in assets folder and link to them**

In this data engineering project, I develop an end-to-end solution to analyse my listening history by building a pipeline to extract my scrobbles from the last.fm API. Firstly, a batch pipeline pulls the last 5 years worth of data. A further pipeline is scheduled to run each day by extracting the previous day's scrobbles and loading them into a BigQuery data set. This then feeds into a Tableau dashboard, which aims to provide some insight into my listening habits. 

Docs for the API can be found here: [:musical_note:](https://www.last.fm/api/intro)

 ## Project objectives
 I aim to answer the following questions:
 
 * What sort of genres do I listen to the most?
 * At what time of the day do I listen to the most music?
 * Has my listening preferences changed over the years?
 * Do my preferences change depending on the season?

## What is last.fm?
A website which records your listening history, with integrations into Spotify, Deezer etc. I've had an account for a very long time dating back to 2013, so it was great to use that historic data in a project. Please support them by making an account and syncing it with your streaming app of choice.

### So, what is a scrobble?
A scrobble is a record of what you listened to, on an individual track level, so each scrobble equals one track played. 

## Data set
The data is extracted from the last.fm API, which is essentially the same listening data [held](https://www.last.fm/user/sorfildor) here on my profile. Follow me over there!

