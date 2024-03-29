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
        {{ get_first_tag("tag") }} as genre_tag

    from source

)

select * from renamed
