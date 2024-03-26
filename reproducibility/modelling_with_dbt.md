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

```
version: 2

sources:
  - name: staging_scrobble
    database: de-zoomcamp-test
    schema: scrobble_data

    tables:
     (you should see 'Generate model' here)
      - name: raw_scrobble_data
...
```

4. Note the ```Generate model``` above. Click this to generate a template for the model creation.
   * You can also define your schema datatypes within ```schema.yml``` before generating

```
models:
  - name: stg_staging_scrobble_data
    description: ""
    columns:
      - name: timestamp
        data_type: timestamp
        description: ""
        tests:
          - not_null:
              severity: warn

      - name: artist
        data_type: string
        description: ""

      - name: artist_mbid
        data_type: string
        description: ""
...
```


### Macros

You may have noticed that in the raw table, the tags are all combined into one string field, separated by commas.
In this form the field is a bit messy and it's hard to extract anything meaningful from it if it was put in a dashboard. The way that last.fm tagging works, 
the first tag is the most popular genre that users have voted for. For sake of simplicity, I'll create a macro that can be used in model creation to simply extract the first
tag. 

Macros are similar to functions that are written in jinja, a templating language similar to python. 

Creating a macro is easy - we'll create a new one in the ```macros``` folder e.g. your_macro.sql

```
{#
    This macro splits the tags 
    and takes the first one as the main tag
#}

{% macro get_first_tag(tag) -%}

SPLIT(tag, ',')[OFFSET(0)] AS tag

{%- endmacro %}

```

 Now simply call it in the generated code

```
with 

source as (

    select * from {{ source('staging_scrobble', 'raw_scrobble_data') }}

),

renamed as (

    select
        cast(timestamp as timestamp) AS timestamp,
        artist,
        artist_mbid,
        track,
        track_mbid,
        album,
        album_mbid,
        {{ get_first_tag("tag") }}

    from source

)

select * from renamed
```

### dbt build
Now we can run ```dbt build``` - dbt will pickup all the models and tests as defined in the current project and execute them in order. 
We can now see the new staging table created in BigQuery.

 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/assets/102922713/40a184c4-024b-4d2f-83ed-f9ee279d3af2" width="700">
 </picture>
 </p>

### Lineage
As you're building your models, dbt will also record the lineage of your models. This is useful to understand how your tables were built from its respective data sources.

 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm-scrobble-analysis/assets/102922713/64296259-1368-4eac-a94c-48627f362cee" width="700">
 </picture>
 </p>

### Creating a fact table
We can aggregate some of the playing history to create a basic fact table containing some useful information for the end-user. 
In this **very** simple example, I'll generate one for the total listens by artist and include some supplementary information such as genre. This won't appear in the final data model, but serves as an example
of what you could do with a more complicated dataset with more potential measures.

This time we'll materialise it as a table, rather than a view:

```
{{
    config(
        materialized='table'
    )
}}

select
    count(*) as total_listens,
    artist,
    tag as genre
  from dbt_jmurray.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3
```

We can create a lot of complicated transformations and thankfully dbt will abstract a lot of the complexity away,
making it syntax-compliant for the destination database regardless of how it's written within dbt.

### Tests
We can also introduce testing in the modelling process. Because I want to ensure that all timestamps are valid, I'll introduce a test to check that there are no nulls in that field.
Under our ```schema.yml``` file, add a test by:

```
...
models:
  - name: stg_staging_scrobble_data
    description: ""
    columns:
      - name: timestamp
        data_type: timestamp
        description: ""
        tests:
          - not_null:
              severity: warn
```

### Documentation
Finally, dbt has a built-in way to generate documentation. Simply run ```dbt docs generate``` and navigate to the documentation tab beside the version control section.

Here you can view a lot of useful information, including the SQL that generated the table, location of source data, macros used, descriptions (if provided) and so on.


## dbt deployment into production

Once we're satisfied with development we can open a request to merge into the main branch. These models can then run in the production environment using the main branch. 
Here's how we'd schedule a production run:

1. Within dbt, we can create a new environment 'PROD', seting the deployment type to ```Production```
2. within the Production environment, create a new job under ```Deploy > Jobs```
3. Here we can create a job to update the production tables and also a ```CI/CD``` job
   * once the jobs run, the changes should be visible within our BigQuery tables


 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/assets/102922713/49d395b2-0987-475a-929a-c2db8f26385a" width="300">
 </picture>
 </p>

## Final data model

 <p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/data%20model.png" width="700">
 </picture>
 </p>

In my data model, the dimension tables could be supplemented with further information to build a more comprehensive and insightful database. The [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API) could be used to retrieve dimensional data based on
the [MBIDs](https://musicbrainz.org/doc/MusicBrainz_Identifier), such as band members or country of origin in the artist table, additional writing credits on the tracks or album table, and instruments used on the track table. 

### Factless Fact Tables
Because the final 'fact' table doesn't contain any measures, it's actually a [factless](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/factless-fact-table/)
fact table. The table itself stores a record of scrobbles and dates, so it allows us aggregate and answer questions such as "how many tracks were listened to on a certain date?" or "how many progressive metal or electronic tracks were listened to?".

## 
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/back.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/reproducibility/mage_orchestration.md)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/next.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
