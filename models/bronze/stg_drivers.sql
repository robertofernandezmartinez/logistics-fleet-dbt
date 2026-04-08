with source as (
    select * from {{ source('raw_logistics', 'drivers') }}
)

select
    driver_id,
    name as driver_name,
    cast(hiring_date as date) as hiring_date
from source
where driver_id is not null