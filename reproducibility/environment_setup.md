 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/section%201.png" width="800">
 </picture>
 </p>


## Google Cloud Platform
For the project you'll need access to a free trial of GCP; you can sign-up [here](https://cloud.google.com/free). Once you have an account, you'll have access to $300 worth of credit. Now, you can create a new project for all your resources associated with the pipeline. 

### Creating a service account
1. Navigate to [IAM & Admin](https://console.cloud.google.com/iam-admin/iam?project=de-zoomcamp-test) and create a new service account with the following credentials:

* Viewer
* Storage Admin
* Storage Object Admin
* BigQuery Admin

2. Download the service account key for authentication purposes. 

3. Install the [Gcloud SDK](https://cloud.google.com/sdk/docs/install-sdk) and set your environment variable pointing to your key:

```
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"

gcloud auth application-default login
```

### Creating a VM - optional
This section isn't strictly necessary as you could run everything locally, however, I also spun up a VM where most of the development took place.

1. Navigate to [Compute Engine](https://console.cloud.google.com/compute/instances?) and rent an instance. I used the following configuration:

> **machine config**
> 
> **boot disk:** Ubuntu, 20.04 LTS, 30gb <br/>
> **machine type:** e2-standard-4 <br/>
> **vCPU:** 4 <br/>
> **Memory:** 16gb

2. Create an [ssh key](https://cloud.google.com/compute/docs/connect/create-ssh-keys#gcloud) to access the VM and add the public key to GCP in compute engine --> metadata --> add ssh key

3. Edit your config file at .ssh/config to match the external ip of the VM instance, then you can simply access it via ssh command or through an IDE e.g. [VSCode](https://medium.com/@ivanzhd/vscode-sftp-connection-to-compute-engine-on-google-cloud-platform-gcloud-9312797d56eb)


   
## Installing requirements
Next install all the project requirements on the VM, this includes:

* [Python 3](https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh)
* Google Cloud SDK - this should be pre-installed on your OS image
* [Docker](https://docs.docker.com/get-docker/) and [Docker compose](https://docs.docker.com/compose/install/)
* [Terraform](https://www.terraform.io/downloads)

##
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/next.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/infrastructure_deployment.md)

