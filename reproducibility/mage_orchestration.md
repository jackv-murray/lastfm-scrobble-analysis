<p align="center">
 <picture>
 <img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/section%204.png" width="800">
 </picture>
 </p>

Now we'll build the pipeline in Mage, an open-source pipeline tool with orchestration, transformation and integration features. Mage separates each distinct phase of a pipeline into testable and reusable blocks of code and has a hybrid development environment, with an interactive GUI. 

## Starting Mage

Either use the mage-ai folder I include or alternatively clone the quick-start repo

```git clone https://github.com/mage-ai/compose-quickstart.git```

1. Navigate to the mage-ai folder and build the mage container ```docker compose build```
2. Start the docker container with ```docker compose up```
3. Navigate to ```localhost:6789``` - you may need to [forward](https://code.visualstudio.com/docs/remote/ssh) this port

## Running the pipeline

The pipeline is configured to run daily to capture the previous day's scrobbles. This is achieved through a date parameter passed to the data_loader block and a trigger which schedules it to run daily. The API key is hidden within Mage's Secrets section,
acting as a secrets manager where I am able to reference it directly in the data_loader block as a variable. 

<p align="center">
 <picture>
 <img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/assets/102922713/431e0c7d-6556-4e60-9a37-000f5ce5f607" width="600">
 </picture>
 </p>
 

## Configuring GCP with Mage

In order to upload to your BigQuery dataset (or GCS Bucket), you'll first need to configure Mage to authenticate with GCP. 
1. Navigate to your io_config.yaml file
2. update the section under Google to include your service account credentials


```
GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/{your_credentials}.json"
GOOGLE_LOCATION: EU # Optional
```

## Deploying Mage on GCP 
Firstly, you'll need a service account with the following permissions:
* Artifact Registry Reader
* Artifact Registry Writer
* BigQuery Admin
* Cloud Run Developer
* Cloud SQL Admin
* Compute Admin
* Service Account Token Creator
* Storage Admin

Once that's created, you can pull down the mage terraform templates via:

```git clone https://github.com/mage-ai/mage-ai-terraform-templates.git```

Now run `terraform init` and `terraform apply` to deploy Mage as a Cloud Run service.

> **General notes**  <br/>
>  You may need to enable several APIs within GCloud Console: Cloud SQL Admin, Serverless VPC Access <br/>
>  You may wish to skip the deployment step - or remember to at least destroy the resources as they are very expensive if left on! <br/>






## 
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/back.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/lastfm_api.md)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/next.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
