<p align="center">
 <picture>
 <img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/section%202.png" width="800">
 </picture>
 </p>

 We'll now use Terraform to deploy the cloud resources required for the project. This can be done manually within the Google Cloud Console, however by using Terraform we can leverage this IaC approach in order to version, re-use and share the configuration files.
 This has the benefit of providing a consistent way to provision and manage the required infrastructure during the pipeline's lifecycle and would make collaboration within a team easier and enhance project oversight. 

 ## Steps

 1. Navigate to the terraform folder and modify the **variables.tf** file
    * In this file you'll specify the variables used in the **main.tf** file
    * Specify your credentials, project name, location, region, resource names - see [here](https://cloud.google.com/docs/terraform/best-practices-for-terraform) for a list of best practices to follow
    * For this project, you'll require a BigQuery data set and a GCS Bucket - specify these in main.tf file
   

   
3. Run ``` terraform init ```
   * This will retrieve the provider plugin i.e. the piece of code that terraform will use to talk to GCP

4. run ``` terraform plan ``` to give a detailed breakdown of the proposed steps

5. Once happy with the above, run ``` terraform apply ```  to deploy the resources
   * The [bucket](https://console.cloud.google.com/storage/) and [BigQuery data set](https://console.cloud.google.com/bigquery?) should now be visible within GCP.
  
### Destroying resources
It's also easy to remove any deployed resources via ```terraform destroy```. Be sure to remove all your resources before your free trial expires!

> **General notes**
> 
> * If you intend to upload your workings publicly, ensure that you amend the .gitignore file to exclude any terraform files containing your credentials e.g. .tfstate <br/>
> * You may need to enable the BigQueryAPI in the console first for Terraform to work

## 
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/back.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/environment_setup.md)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/next.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/lastfm_api.md)
