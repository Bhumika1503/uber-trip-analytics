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