 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/section%205.png" width="800">
 </picture>
 </p>

In this section we'll use dbt (data build tool) to model our data that we've extracted and loaded into our data warehouse. We'll then create dimension and fact tables in accordance with
[Kimball modelling](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/star-schema-olap-cube/) principles. 

dbt is a powerful tool that allows anyone that knows SQL to transform data whilst following software engineering best practices such as modularity, portability, CI/CD, and documentation. It simply sits on top of our
data warehouse and helps us to transform the raw data into something useful for business users. 

Each 'model' is simply a .sql file containing **SELECT statements only**, therefore it abstracts away a lot of the complexity of DDL/DML.

## Getting started with dbt

1. Firstly, create a [new](https://console.cloud.google.com/iam-admin/) service account for dbt with the BigQuery Admin role and generate a key
2. create a [new](https://www.getdbt.com/signup) dbt account
3. create a new dbt cloud project, selecting BigQuery as your data warehouse connection type
4. next, upload your service account key, which will pre-populate most fields
5. now you'll have the option of using a dbt-managed repository, or adding your [own](https://docs.getdbt.com/docs/cloud/git/connect-github)

Now you should be set-up to start developing in dbt cloud.

## dbt development

To begin, initialise your project and create a new branch. Now we'll create our first model.

1. On the right hand side you'll see the ```File explorer```. Create a new folder within the ```models``` folder.
2. within the new folder, create a new file ```schema.yml```
3. enter the details for your BigQuery table - the one which the pipeline exported to


 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/assets/102922713/82517457-f5eb-476c-a7b9-531ffc02a942" width="300">
 </picture>
 </p>

4. Note the ```Generate model``` above. Click this to generate a template for the model creation.
   * You can also define your schema datatypes within ```schema.yml``` before generating


 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/assets/102922713/c4c5bb0f-00fb-4f71-890b-9e5345e1db2c" width="300">
 </picture>
 </p>


### Macros

You may have noticed that in the raw output files, the tags are all combined into one string field from a comma separated list.
In this form the field is a bit messy and it's hard to extract anything meaningful from it if it was put in a dashboard. The way that last.fm tagging works, 
the first tag is the most popular genre that users have voted on  
