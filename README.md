# Uber Trip Analytics Pipeline

An end-to-end data engineering project that extracts Uber trip data, validates and transforms it, loads it into a PostgreSQL data warehouse, performs analytical processing using Apache Spark, and visualizes insights through a multi-page Streamlit dashboard.

The pipeline is orchestrated using Apache Airflow, providing a complete workflow from data ingestion to analytics.

---

## Project Overview

The objective of this project is to build a complete data engineering pipeline for analyzing Uber trip data.

The system demonstrates the following data engineering workflow:

1. Data extraction from an external data source
2. Data validation
3. Data transformation
4. Loading transformed data into PostgreSQL
5. Data warehousing using a structured warehouse schema
6. Analytical processing using PySpark
7. Workflow orchestration using Apache Airflow
8. Interactive visualization using Streamlit

The project demonstrates how different components of a modern data engineering stack work together in an end-to-end pipeline.

---

## Architecture

                    Data Source
                        |
                        v
                +---------------+
                |    Extract    |
                +---------------+
                        |
                        v
                +---------------+
                |   Validate    |
                +---------------+
                        |
                        v
                +---------------+
                |  Transform    |
                +---------------+
                        |
                        v
                +---------------+
                |  PostgreSQL   |
                | Data Warehouse|
                +---------------+
                        |
              +---------+---------+
              |                   |
              v                   v
       +-------------+     +-------------+
       |   PySpark   |     |  Streamlit  |
       |  Analytics  |     |  Dashboard  |
       +-------------+     +-------------+
              ^
              |
       +-------------+
       |  Airflow    |
       | Orchestration|
       +-------------+

### Pipeline Workflow

Airflow
   |
   +--> ETL Pipeline
   |      |
   |      +--> Extract
   |      +--> Validate
   |      +--> Transform
   |      +--> Load to PostgreSQL
   |
   +--> Spark Analytics
          |
          +--> Revenue Analysis
          +--> Pickup Hour Analysis

---

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | ETL and application development |
| PostgreSQL | Data warehouse and analytical storage |
| Apache Airflow | Pipeline orchestration |
| Apache Spark / PySpark | Data processing and analytics |
| Streamlit | Interactive dashboard |
| Pandas | Data manipulation |
| SQL | Data transformation and analytical queries |
| JDBC | Spark-to-PostgreSQL connectivity |
| python-dotenv | Environment configuration |
| Git / GitHub | Version control |

---

## Project Structure

uber-trip-analytics/
│
├── main.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── raw/
│
├── sql/
│   └── ...
│
├── spark/
│   ├── __init__.py
│   ├── main.py
│   ├── reader.py
│   ├── reports.py
│   └── session.py
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── db_connection.py
│   ├── metrics.py
│   ├── queries.py
│   ├── tables.py
│   │
│   └── pages/
│       ├── 1_Demand_Analysis.py
│       ├── 2_Revenue_Analysis.py
│       ├── 3_Trip_Analysis.py
│       ├── 4_Location_Analysis.py
│       └── 5_Ride_Type_Analysis.py
│
├── dags/
│   └── uber_trip_pipeline.py
│
└── drivers/
    └── postgresql-42.7.13.jar

---

## Data Pipeline

### 1. Data Extraction

The pipeline extracts Uber trip data from the configured external data source and prepares the records for downstream processing.

### 2. Data Validation

The extracted data is validated before transformation to ensure that the incoming records are suitable for further processing.

Example output:

Rows Extracted : 500
Validation Successful

### 3. Data Transformation

The transformation layer prepares the extracted data for analytical storage.

Transformations include processing fields such as:

- Pickup and drop-off timestamps
- Pickup and drop-off dates
- Pickup hour
- Pickup and drop-off locations
- Trip distance
- Trip duration
- Revenue-related fields
- Ride-sharing indicators

Example output:

Rows After Transformation : 500
Transformation Successful

### 4. PostgreSQL Data Warehouse

The transformed data is loaded into PostgreSQL.

The primary analytical fact table is:

warehouse.fact_trips

This table serves as the main analytical source for PySpark and the Streamlit dashboard.

---

## PySpark Analytics

Apache Spark is used to perform analytical processing on the warehouse data.

The Spark application reads data from:

warehouse.fact_trips

through the PostgreSQL JDBC connection.

Current analytical operations include:

- Revenue analysis
- Busiest pickup hour analysis

The Spark implementation is organized as:

spark/
├── __init__.py
├── main.py
├── reader.py
├── reports.py
└── session.py

---

## Apache Airflow

Apache Airflow is used to orchestrate the pipeline.

The DAG is:

uber_trip_pipeline

The current workflow is:

run_etl_pipeline
        |
        v
run_spark_analytics

The ETL task runs first and loads the transformed data into PostgreSQL.

After successful completion of the ETL task, the Spark analytics task is executed.

---

## Streamlit Dashboard

The project includes a multi-page Streamlit dashboard for exploring analytical results.

### Dashboard Structure

Dashboard
│
├── Overview
│
├── Demand Analysis
│
├── Revenue Analysis
│
├── Trip Analysis
│
├── Location Analysis
│
└── Ride Type Analysis

### Overview

Provides high-level KPIs and an overall view of trip activity.

### Demand Analysis

Focuses on trip demand patterns and peak activity periods.

### Revenue Analysis

Provides revenue-focused analysis and trends.

### Trip Analysis

Analyzes trip characteristics such as distance and duration.

### Location Analysis

Provides pickup, drop-off, and route-based analysis.

### Ride Type Analysis

Analyzes available ride-type characteristics in the dataset.

---

## Running the Project

### 1. Clone the Repository

git clone <repository-url>
cd uber-trip-analytics

### 2. Create and Activate Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

WSL/Linux:

python -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a .env file:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=uber_analytics
DB_USER=postgres
DB_PASSWORD=your_password

### 5. Run ETL

python main.py

### 6. Run Spark Analytics

python -m spark.main

### 7. Run Dashboard

streamlit run dashboard/app.py

### 8. Run with Airflow

Start Airflow and trigger the uber_trip_pipeline DAG.

Pipeline flow:

ETL → Spark Analytics

---

## Key Engineering Concepts Demonstrated

- End-to-end ETL pipeline development
- Data validation and transformation
- PostgreSQL data warehousing
- SQL-based analytics
- JDBC connectivity
- PySpark data processing
- Apache Airflow orchestration
- Airflow task dependencies
- Environment-based configuration
- Interactive data visualization
- Modular Python architecture
- Windows and WSL-based development

---

## Future Improvements

- Advanced data quality checks
- Pipeline monitoring and failure alerts
- Spark performance optimization
- Cloud deployment using Azure or AWS
- Docker containerization

---

## Author

### Bhumika Chauhan

B.Tech Computer Science Engineering

Data Engineering | Python | SQL | PostgreSQL | PySpark | Apache Airflow