{{
    config(
        materialized='table'
    )
}}

select
        album as album_name,
        album_mbid
  from 'your_bq_database'.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3