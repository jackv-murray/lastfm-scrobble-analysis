{{
    config(
        materialized='table'
    )
}}

select
        timestamp
        artist as artist_name,
        artist_mbid,
        track as track_name,
        track_mbid,
        album album_name,
        album_mbid,
        genre_tag
  from 'your_bq_database'.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3

