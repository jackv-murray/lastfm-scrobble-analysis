variable "credentials" {
  description = "my credentials"
  #point to your gc credentials
  default     = ".json"
}

variable "project" {
  description = "name of project"
  default     = " "
}

#enter your designed location and region
variable "location" {
  description = "project location"
  default     = "EU"
}

variable "region" {
  description = "region location"
  default     = "europe-west2-a"
}

variable "bq_dataset_name" {
  description = "name of the bq data set"
  default     = " "
}

variable "gcs_bucket_name" {
  description = "name of the bucket"
  default     = " "
}

variable "gcs_storage_class" {
  description = "bucket storage class"
  default     = "STANDARD"
}