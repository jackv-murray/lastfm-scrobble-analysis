{{
    config(
        materialized='table'
    )
}}

select
        genre_tag

  from 'your_bq_database'.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3