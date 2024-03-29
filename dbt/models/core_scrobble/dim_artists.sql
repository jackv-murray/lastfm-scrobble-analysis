{{
    config(
        materialized='table'
    )
}}

select
        artist as artist_name,
        artist_mbid
  from 'your_bq_database'.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3