<p align="center">
 <picture>
<img src="https://github.com/jackv-murray/lastfm-scrobble-analysis/assets/102922713/f3815561-07b2-45b0-8600-8ef58d7f3383" width="800">
 </picture>
 </p>

## Lakehouse structure
To maintain an overall structure that more resembles a [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture) design, I could have extracted and stored the raw data differently into a Bronze Layer. For ease of use, I implement a step to flatten the data before loading into GCS, but in future it may have been worth storing the raw JSONs in the lakehouse, which would make it easier to reconstruct the data in the future from the raw files. 

If I was dealing with larger files, it may have been better to store in an alternative format, such as parquet. 

## Modelling
The extracted data contains [MBIDs](https://musicbrainz.org/doc/MusicBrainz_Identifier), and so the overall data model could have been supplemented further with the [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API) data to pull more information for the dimensional tables.

## Orchestration
There were many features in Mage that could have been used to improve the overall pipeline. The ability to create notifications when a pipeline failed would be useful in a production environment. Also, Mage supports dbt natively and so the dbt processing could have been included in the orchestration step. 

## Testing
Adding more tests for each block of the pipeline, and more testing within dbt to make the entire process more robust and reliable.


## 
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/back.png" width="80">](https://github.com/jackv-murray/lastfm-scrobble-analysis/blob/main/reproducibility/data_visualisation.md)
[<img src="https://github.com/jackv-murray/lastfm_scrobble_analysis/blob/main/assets/home.png" width="80">](https://github.com/jackv-murray/lastfm_scrobble_analysis)
