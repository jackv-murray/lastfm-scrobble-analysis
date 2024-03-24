# Tools used

Below are the tools used for this project.

## [<img src="https://wiki.coreelec.org/_media/coreelec:docker.png?w=380&tok=ea2958" width="200">](https://www.docker.com/)
Docker was used a lot during the development phase in order to manage dependencies which was very useful when initially testing/developing locally to switching development to the cloud VM instance. Having just one configuration and an easy way of deploying everything in a lightweight container greatly simplified the entire process.

## [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Terraform_Logo.svg/1280px-Terraform_Logo.svg.png" width="200">](https://www.terraform.io/)
Terraform, a Infrastructure as Code (IaC) tool, was used to deploy various cloud resources in a convenient and reproducible way. 


## [<img src="https://mintlify.s3-us-west-1.amazonaws.com/mage/logo/light.svg" width="200">](https://www.mage.ai/) 
Mage is the orchestrator of choice, where the pipeline is built with a trigger scheduling it to run as specified. 


## [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Google_Cloud_logo.svg/1280px-Google_Cloud_logo.svg.png" width="200">](https://cloud.google.com/?hl=en) 
Everything is running on Google Cloud. I make use of a VM instance for the initial testing and development phase.  Mage is also deployed as a cloud resource using Cloud Run. Cloud storage is my data lake and the data is held within Big Query, the data warehouse. 


## [<img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png" width="200">](https://www.tableau.com/en-gb) 
This is my data visualisation tool of choice. Why Tableau? Mostly because I already use it professionally and have a lot of experience building dashboards. Also, so I can add the final viz to my Tableau public portfolio. 
