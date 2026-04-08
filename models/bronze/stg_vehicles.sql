with source as (
    select * from {{ source('raw_logistics', 'vehicles') }}
)

select
    vehicle_id,
    model as vehicle_model,
    fuel_capacity_l
from source
where vehicle_id is not null