import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Settings
NUM_TRIPS = 50000
NUM_VEHICLES = 50
NUM_DRIVERS = 30

# 1. Generate Vehicles (Masters)
vehicles = pd.DataFrame({
    'vehicle_id': [f'V{str(i).zfill(3)}' for i in range(1, NUM_VEHICLES + 1)],
    'model': np.random.choice(['Volvo FH', 'Scania R500', 'MAN TGX', 'Mercedes Actros'], NUM_VEHICLES),
    'fuel_capacity_l': np.random.randint(400, 800, NUM_VEHICLES)
})

# 2. Generate Drivers (Masters)
drivers = pd.DataFrame({
    'driver_id': [f'D{str(i).zfill(2)}' for i in range(1, NUM_DRIVERS + 1)],
    'name': [f'Driver {i}' for i in range(1, NUM_DRIVERS + 1)],
    'hiring_date': [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1500)) for _ in range(NUM_DRIVERS)]
})

# 3. Generate Trips (The Messy Fact Table)
dates = [datetime(2025, 1, 1) + timedelta(minutes=np.random.randint(0, 600000)) for _ in range(NUM_TRIPS)]

trips = pd.DataFrame({
    'trip_id': [f'T{str(i).zfill(6)}' for i in range(1, NUM_TRIPS + 1)],
    'vehicle_id': np.random.choice(vehicles['vehicle_id'], NUM_TRIPS),
    'driver_id': np.random.choice(drivers['driver_id'], NUM_TRIPS),
    'distance_km': np.random.uniform(10, 1200, NUM_TRIPS),
    'fuel_liters': np.random.uniform(5, 350, NUM_TRIPS),
    'trip_date': dates
})

# --- INJECTING ERRORS (The "Dirty" Part) ---
# Duplicate some records (1%)
duplicates = trips.sample(int(NUM_TRIPS * 0.01))
trips = pd.concat([trips, duplicates])

# Add Outliers (Heavy foot drivers or sensor errors)
trips.loc[trips.sample(100).index, 'fuel_liters'] = 9999 

# Mess up date formats (Some to string DD/MM/YYYY)
trips['trip_date'] = trips['trip_date'].dt.strftime('%Y-%m-%d')
trips.loc[trips.sample(500).index, 'trip_date'] = '01/01/2026'

# Add Nulls
trips.loc[trips.sample(200).index, 'distance_km'] = np.nan

# Save to CSV
trips.to_csv('raw_trips.csv', index=False)
vehicles.to_csv('raw_vehicles.csv', index=False)
drivers.to_csv('raw_drivers.csv', index=False)

print(f"Success! Generated {len(trips)} rows with intentional errors.")