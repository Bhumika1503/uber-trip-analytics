import streamlit as st

from db_connection import run_query

from queries import (
    KPI_QUERY,
    PAYMENT_QUERY,
    VENDOR_QUERY,
    DISTANCE_QUERY,
    TOP_PICKUP_QUERY
)

from metrics import show_metrics

from charts import (
    payment_chart,
    vendor_chart,
    distance_chart
)

from tables import pickup_table


st.set_page_config(
    page_title="Uber Trip Analytics",
    page_icon="🚖",
    layout="wide"
)


st.sidebar.title("🚖 Uber Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "About"
    ]
)


if page == "Dashboard":

    st.title("🚖 Uber Trip Analytics Dashboard")

    st.divider()

    kpi_df = run_query(KPI_QUERY)

    show_metrics(kpi_df)

    st.divider()

    with st.expander("💳 Revenue Analysis", expanded=True):

        payment_df = run_query(PAYMENT_QUERY)

        payment_chart(payment_df)

    with st.expander("🚕 Vendor Analysis", expanded=True):

        vendor_df = run_query(VENDOR_QUERY)

        vendor_chart(vendor_df)

    with st.expander("📏 Distance Analysis", expanded=True):

        distance_df = run_query(DISTANCE_QUERY)

        distance_chart(distance_df)

    with st.expander("📍 Top Pickup Locations", expanded=True):

        pickup_df = run_query(TOP_PICKUP_QUERY)

        pickup_table(pickup_df)

# ---------------- About ---------------- #

st.title("🚖 Uber Trip Analytics")

st.markdown("""
## End-to-End Data Engineering Project

This project demonstrates how raw Uber trip data can be transformed into meaningful business insights through a modern data engineering pipeline.

### Tech Stack

- 🐍 Python
- 🗄 PostgreSQL
- ⚡ Apache Spark
- 📊 Streamlit
- 🔗 SQLAlchemy
- 📑 Pandas

### Features

- Automated ETL Pipeline
- PostgreSQL Data Warehouse
- Spark-based Data Processing
- Interactive Dashboard
- SQL Analytics

### Future Enhancements

- Apache Airflow for Workflow Scheduling
- Automated Multi-file Processing
- Dashboard Filters and Advanced Visualizations
- Docker Deployment

---

Developed as a portfolio project to demonstrate practical Data Engineering concepts.
""")