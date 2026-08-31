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

The project is designed to demonstrate how different components of a modern data engineering stack work together in an end-to-end pipeline.

---

## Architecture

```text
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
---


##  Technology Stack
Technology	Purpose
Python	ETL and application development
PostgreSQL	Data warehouse and analytical storage
Apache Airflow	Pipeline orchestration
Apache Spark / PySpark	Distributed data processing and analytics
Streamlit	Interactive dashboard
Pandas	Data manipulation
SQL	Data transformation and analytical queries
JDBC	Spark-to-PostgreSQL connectivity
python-dotenv	Environment configuration
Git / GitHub	Version control

Streamlit Dashboard

The project includes a multi-page Streamlit dashboard for exploring analytical results.

Dashboard Structure
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

## Running the Project

### 1. Clone the repository
git clone <repository-url>
cd uber-trip-analytics

### 2. Create and activate virtual environment

Windows:
python -m venv venv
venv\Scripts\activate

WSL/Linux:
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure `.env`

### 5. Run ETL
python main.py

### 6. Run Spark Analytics
python -m spark.main

### 7. Run Dashboard
streamlit run dashboard/app.py

### 8. Run with Airflow
Start Airflow and trigger the `uber_trip_pipeline` DAG.

Pipeline flow:
ETL → Spark Analytics

## Future Improvements

- Advanced data quality checks
- Pipeline monitoring and failure alerts
- Spark performance optimization
- Cloud deployment using Azure or AWS
- Docker containerization

## Author

### Bhumika Chauhan

B.Tech Computer Science Engineering  
Data Engineering | Python | SQL | PostgreSQL | PySpark | Apache Airflow
