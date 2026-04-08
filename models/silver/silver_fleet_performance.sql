with trips as (
    select * from {{ ref('stg_trips') }}
),

vehicles as (
    select * from {{ ref('stg_vehicles') }}
),

drivers as (
    select * from {{ ref('stg_drivers') }}
),

joined as (
    select
        t.trip_id,
        t.trip_date,
        v.vehicle_model,
        d.driver_name,
        t.distance_km,
        t.fuel_liters,
        -- Key Business KPI: Liters per 100km
        safe_divide(t.fuel_liters, t.distance_km) * 100 as fuel_efficiency_100km
    from trips t
    left join vehicles v on t.vehicle_id = v.vehicle_id
    left join drivers d on t.driver_id = d.driver_id
)

select * from joined
where fuel_efficiency_100km is not null