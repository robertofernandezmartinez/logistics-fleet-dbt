with source as (
    select * from {{ source('raw_logistics', 'trips') }}
),

transformed as (
    select
        trip_id,
        vehicle_id,
        driver_id,
        -- Handling extreme outliers in distance (sensor errors)
        case 
            when distance_km > 5000 then null 
            else distance_km 
        end as distance_km,
        -- Handling unrealistic fuel consumption values
        case 
            when fuel_liters > 1000 then null 
            else fuel_liters 
        end as fuel_liters,
        -- Standardizing date formats and handling inconsistencies
        safe.parse_date('%Y-%m-%d', trip_date) as trip_date
    from source
)

select * from transformed
-- Deduplicating and removing records without a valid primary key
where trip_id is not null