# [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Lastfm_logo.svg/2560px-Lastfm_logo.svg.png" width="80">](https://last.fm) scrobble analysis 
last.fm scrobble analysis looking at my own listening habits!

**replace logos with copies in assets folder and link to them**

# Project Description
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

# Tools used

Below are the tools used for this project. Where applicable, all scripting was done in Python.

## [<img src="https://wiki.coreelec.org/_media/coreelec:docker.png?w=380&tok=ea2958" width="200">](https://www.docker.com/)
Docker is used a lot during the development phase in order to manage dependencies and easily deploy various containers for
.
## [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Terraform_Logo.svg/1280px-Terraform_Logo.svg.png" width="200">](https://www.terraform.io/)
Terraform, a Infrastructure as Code (IaC) tool, is used to deploy various cloud resources in a convenient and reproducible way. 


## [<img src="https://mintlify.s3-us-west-1.amazonaws.com/mage/logo/light.svg" width="200">](https://www.mage.ai/) 
Mage is the orchestrator of choice, where the pipeline is built with a trigger scheduling it to run as specified. 


## [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" width="200">](https://cloud.google.com/?hl=en) 
Everything is running on Google Cloud. I make use of a VM instance for the initial testing and development phase.  Mage is also deployed as a cloud resource using Cloud Run. Cloud storage is my data lake and the data is held within Big Query, the data warehouse. 


## [<img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png" width="200">](https://www.tableau.com/en-gb) 
This is my data visualisation tool of choice. Why Tableau? Mostly because I already use it professionally and have a lot of experience building dashboards. Also, so I can add the final viz to my Tableau public portfolio. 
