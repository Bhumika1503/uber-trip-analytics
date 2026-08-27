import streamlit as st
import pandas as pd

from db_connection import run_query


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Uber Trip Analytics",
    page_icon="🚕",
    layout="wide"
)


# ---------------------------------------------------------
# Styling
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    [data-testid="stMetric"] {
        background-color: #F7F8FA;
        border: 1px solid #E5E7EB;
        padding: 18px;
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🚕 Uber Trip Analytics")

st.markdown(
    "### Real-time analytical overview of Uber trip activity"
)

st.caption(
    "Data Source: NYC Open Data • PostgreSQL Data Warehouse"
)

st.divider()


# ---------------------------------------------------------
# KPI Query
# ---------------------------------------------------------

KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,

    COALESCE(
        ROUND(SUM(total_revenue)::numeric, 2),
        0
    ) AS total_revenue,

    COALESCE(
        ROUND(AVG(total_revenue)::numeric, 2),
        0
    ) AS average_trip_value,

    COALESCE(
        ROUND(AVG(trip_miles)::numeric, 2),
        0
    ) AS average_distance,

    COALESCE(
        ROUND(AVG(trip_duration_minutes)::numeric, 2),
        0
    ) AS average_duration

FROM warehouse.fact_trips;
"""


kpi_df = run_query(KPI_QUERY)


# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

if not kpi_df.empty:

    row = kpi_df.iloc[0]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "🚕 Total Trips",
        f"{int(row['total_trips']):,}"
    )

    col2.metric(
        "💰 Total Revenue",
        f"${float(row['total_revenue']):,.2f}"
    )

    col3.metric(
        "💵 Avg Trip Value",
        f"${float(row['average_trip_value']):,.2f}"
    )

    col4.metric(
        "📏 Avg Distance",
        f"{float(row['average_distance']):,.2f} mi"
    )

    col5.metric(
        "⏱️ Avg Duration",
        f"{float(row['average_duration']):,.2f} min"
    )

else:

    st.warning("No trip data available.")


st.divider()


# ---------------------------------------------------------
# Hourly Demand
# ---------------------------------------------------------

st.subheader("📈 Trip Demand by Hour")

HOUR_QUERY = """
SELECT
    pickup_hour,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_hour IS NOT NULL
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

hour_df = run_query(HOUR_QUERY)

if not hour_df.empty:

    hour_df["pickup_hour"] = hour_df["pickup_hour"].astype(int)

    st.line_chart(
        hour_df.set_index("pickup_hour")["total_trips"]
    )

else:

    st.info("No hourly data available.")


# ---------------------------------------------------------
# Revenue vs Trips
# ---------------------------------------------------------

st.subheader("💰 Revenue Overview")

REVENUE_QUERY = """
SELECT
    pickup_date,
    COUNT(*) AS total_trips,
    ROUND(SUM(total_revenue)::numeric, 2) AS total_revenue
FROM warehouse.fact_trips
WHERE pickup_date IS NOT NULL
GROUP BY pickup_date
ORDER BY pickup_date;
"""

revenue_df = run_query(REVENUE_QUERY)

if not revenue_df.empty:

    revenue_df["pickup_date"] = pd.to_datetime(
        revenue_df["pickup_date"]
    )

    revenue_df = revenue_df.set_index("pickup_date")

    st.line_chart(
        revenue_df[
            ["total_trips", "total_revenue"]
        ]
    )

else:

    st.info("No revenue data available.")


# ---------------------------------------------------------
# Top Pickup Locations
# ---------------------------------------------------------

st.subheader("📍 Top Pickup Locations")

LOCATION_QUERY = """
SELECT
    pickup_location,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_location IS NOT NULL
GROUP BY pickup_location
ORDER BY total_trips DESC
LIMIT 10;
"""

location_df = run_query(LOCATION_QUERY)

if not location_df.empty:

    st.bar_chart(
        location_df.set_index("pickup_location")
    )

else:

    st.info("No location data available.")


st.divider()

st.caption(
    "Uber Trip Analytics • Built with Python, PostgreSQL, "
    "PySpark and Streamlit"
)