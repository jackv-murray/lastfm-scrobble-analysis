{{
    config(
        materialized='table'
    )
}}

select
        timestamp as scrobble_time,
        extract(month from timestamp) as month,
        extract(year from timestamp) as year

  from 'your_bq_database'.stg_staging_scrobble__raw_scrobble_data

  group by 2, 3