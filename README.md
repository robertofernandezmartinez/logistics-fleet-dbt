# Logistics Fleet Data Engine 🚛

End-to-end data transformation pipeline built with **dbt**, **BigQuery**, and **Python**. This project simulates a real-world logistics scenario, processing 50,000+ trip records to analyze fuel efficiency across a commercial fleet.

## 🏗️ Architecture (Medallion Approach)
The project follows the Medallion Architecture to ensure data quality and scalability:

- **Bronze (Staging):** Schema standardization, technical cleaning, and date normalization using `SAFE.PARSE_DATE`.
- **Silver (Intermediate):** Business logic integration. Joins trips, vehicles, and drivers tables to calculate the key KPI: `fuel_efficiency_100km`.
- **Gold (Marts):** Aggregated business metrics for stakeholders (Efficiency by driver and vehicle model).

## 🛠️ Tech Stack
- **Data Transformation:** dbt (Data Build Tool)
- **Warehouse:** Google BigQuery
- **Environment:** Conda
- **Data Generation:** Python (Pandas/Numpy)
- **Visualization:** Looker Studio

## 🧪 Data Quality & Testing
Robustness is guaranteed through dbt tests:
- **Generic Tests:** `not_null` and `unique` on primary keys.
- **Business Tests:** `dbt_utils.accepted_range` to ensure fuel consumption and distances fall within realistic physical bounds (e.g., 0 to 200 L/100km).

## 🚀 How to Run
1. Clone the repo.
2. Setup your `profiles.yml` for BigQuery.
3. Install dependencies: `dbt deps`.
4. Run the pipeline: `dbt run`.
5. Execute tests: `dbt test`.