# Logistics Fleet Data Engine on dbt 🚛

End-to-end data transformation pipeline built with **dbt**, **BigQuery**, and **Python**. This project simulates a real-world logistics scenario, processing 50,000+ trip records to analyze fuel efficiency across a commercial fleet.


## 🏗️ Data Architecture & Modeling

The project is structured following the **Medallion Architecture** to ensure data traceability and quality:

**1. BRONZE Layer (Staging)**
* `stg_trips`: Technical cleansing, date normalization, and sensor error filtering.
* `stg_vehicles`: Standardization of truck fleet metadata.
* `stg_drivers`: Processing of driver master records.

**2. SILVER Layer (Intermediate)**
* `silver_fleet_performance`: Integration table joining telemetry (trips) with dimensions (drivers and vehicles). Includes fuel efficiency business logic and outlier handling.

**3. GOLD Layer (Marts)**
* `gold_fleet_stats`: Final reporting table for business stakeholders. Contains aggregated metrics and performance rankings by model and driver.


## 👷🏻‍♂️ Transformation Summary

| Layer | Input | Output | Key Operations |
| :--- | :--- | :--- | :--- |
| **Bronze** | Raw Data | `stg_` | `SAFE.PARSE_DATE`, casting, and initial validation. |
| **Silver** | Staging | `silver_` | Massive `LEFT JOIN` and `L/100km` calculation. |
| **Gold** | Silver | `gold_` | `GROUP BY` and performance ranking aggregation. |


## 🧪 Data Quality & Testing
Robustness is guaranteed through dbt tests:
- **Generic Tests:** `not_null` and `unique` on primary keys.
- **Business Tests:** `dbt_utils.accepted_range` to ensure fuel consumption and distances fall within realistic physical bounds (e.g., 0 to 200 L/100km).


## 🛠️ Tech Stack
- **Data Transformation:** dbt (Data Build Tool)
- **Warehouse:** Google BigQuery
- **Environment:** Conda
- **Data Generation:** Python (Pandas/Numpy)
- **Visualization:** Looker Studio


## 📦 Dependencies & Packages
This project utilizes the following **dbt packages** to extend functionality:
* **dbt-utils:** Used for advanced data quality testing (`accepted_range`) and cross-database macros.


## 🚀 How to Run
1. Clone the repo.
2. Setup your `profiles.yml` for BigQuery.
3. Install dependencies: `dbt deps`.
4. Run the pipeline: `dbt run`.
5. Execute tests: `dbt test`.