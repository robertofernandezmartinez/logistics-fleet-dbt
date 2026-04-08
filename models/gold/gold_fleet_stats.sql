with silver_data as (
    select * from {{ ref('silver_fleet_performance') }}
),

final_metrics as (
    select
        vehicle_model,
        driver_name,
        -- Aggregated metrics
        count(trip_id) as total_trips,
        sum(distance_km) as total_km,
        sum(fuel_liters) as total_fuel_consumed,
        -- Efficiency KPI
        avg(fuel_efficiency_100km) as avg_efficiency_100km
    from silver_data
    group by 1, 2
)

select * from final_metrics
order by avg_efficiency_100km asc