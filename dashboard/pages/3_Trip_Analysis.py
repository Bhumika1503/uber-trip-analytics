import streamlit as st
import pandas as pd
import plotly.express as px

from db_connection import run_query

st.set_page_config(
    page_title="Trip Analysis",
    page_icon="🚕",
    layout="wide"
)

PRIMARY = "#2F7D7A"
SECONDARY = "#64748B"

st.title("🚕 Trip Analysis")
st.markdown("Analyze trip distance, duration and fare efficiency.")
st.divider()

KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,
    ROUND(AVG(trip_miles)::numeric, 2) AS avg_distance,
    ROUND(AVG(trip_duration_minutes)::numeric, 2) AS avg_duration,
    ROUND(MAX(trip_miles)::numeric, 2) AS max_distance,
    ROUND(MAX(trip_duration_minutes)::numeric, 2) AS max_duration
FROM warehouse.fact_trips
WHERE trip_miles IS NOT NULL
AND trip_duration_minutes IS NOT NULL
AND trip_miles >= 0
AND trip_duration_minutes >= 0;
"""

kpi_df = run_query(KPI_QUERY)

if not kpi_df.empty:
    row = kpi_df.iloc[0]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "🚕 Total Trips",
        f"{int(row['total_trips']):,}"
    )

    col2.metric(
        "📏 Avg Distance",
        f"{float(row['avg_distance']):.2f} mi"
    )

    col3.metric(
        "⏱️ Avg Duration",
        f"{float(row['avg_duration']):.2f} min"
    )

    col4.metric(
        "📍 Longest Trip",
        f"{float(row['max_distance']):.2f} mi"
    )

    col5.metric(
        "⏱️ Longest Duration",
        f"{float(row['max_duration']):.2f} min"
    )

st.divider()

st.subheader("Trip Distance Distribution")

DISTANCE_QUERY = """
SELECT
    trip_miles
FROM warehouse.fact_trips
WHERE trip_miles IS NOT NULL
AND trip_miles >= 0;
"""

distance_df = run_query(DISTANCE_QUERY)

if not distance_df.empty:
    distance_df["trip_miles"] = pd.to_numeric(
        distance_df["trip_miles"],
        errors="coerce"
    )

    distance_df = distance_df.dropna()

    fig = px.histogram(
        distance_df,
        x="trip_miles",
        nbins=30,
        labels={
            "trip_miles": "Distance (miles)"
        }
    )

    fig.update_traces(marker_color=PRIMARY)

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("Trip Duration Distribution")

DURATION_QUERY = """
SELECT
    trip_duration_minutes
FROM warehouse.fact_trips
WHERE trip_duration_minutes IS NOT NULL
AND trip_duration_minutes >= 0;
"""

duration_df = run_query(DURATION_QUERY)

if not duration_df.empty:
    duration_df["trip_duration_minutes"] = pd.to_numeric(
        duration_df["trip_duration_minutes"],
        errors="coerce"
    )

    duration_df = duration_df.dropna()

    fig = px.histogram(
        duration_df,
        x="trip_duration_minutes",
        nbins=30,
        labels={
            "trip_duration_minutes": "Duration (minutes)"
        }
    )

    fig.update_traces(marker_color=SECONDARY)

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("Distance vs Trip Duration")

EFFICIENCY_QUERY = """
SELECT
    trip_miles,
    trip_duration_minutes,
    total_revenue
FROM warehouse.fact_trips
WHERE trip_miles IS NOT NULL
AND trip_duration_minutes IS NOT NULL
AND total_revenue IS NOT NULL
AND trip_miles >= 0
AND trip_duration_minutes > 0
AND total_revenue >= 0;
"""

efficiency_df = run_query(EFFICIENCY_QUERY)

if not efficiency_df.empty:
    efficiency_df["trip_miles"] = pd.to_numeric(
        efficiency_df["trip_miles"],
        errors="coerce"
    )

    efficiency_df["trip_duration_minutes"] = pd.to_numeric(
        efficiency_df["trip_duration_minutes"],
        errors="coerce"
    )

    efficiency_df["total_revenue"] = pd.to_numeric(
        efficiency_df["total_revenue"],
        errors="coerce"
    )

    efficiency_df = efficiency_df.dropna()

    fig = px.scatter(
        efficiency_df,
        x="trip_duration_minutes",
        y="trip_miles",
        size="total_revenue",
        opacity=0.65,
        labels={
            "trip_duration_minutes": "Duration (minutes)",
            "trip_miles": "Distance (miles)",
            "total_revenue": "Revenue ($)"
        }
    )

    fig.update_traces(
        marker=dict(
            color=PRIMARY,
            size=8
        )
    )

    fig.update_layout(
        template="simple_white",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("Revenue per Mile")

REVENUE_MILE_QUERY = """
SELECT
    trip_miles,
    total_revenue,
    ROUND(
        (total_revenue / NULLIF(trip_miles, 0))::numeric,
        2
    ) AS revenue_per_mile
FROM warehouse.fact_trips
WHERE trip_miles > 0
AND total_revenue >= 0;
"""

revenue_mile_df = run_query(REVENUE_MILE_QUERY)

if not revenue_mile_df.empty:
    revenue_mile_df["revenue_per_mile"] = pd.to_numeric(
        revenue_mile_df["revenue_per_mile"],
        errors="coerce"
    )

    revenue_mile_df = revenue_mile_df.dropna()

    fig = px.histogram(
        revenue_mile_df,
        x="revenue_per_mile",
        nbins=30,
        labels={
            "revenue_per_mile": "Revenue per Mile ($)"
        }
    )

    fig.update_traces(marker_color=PRIMARY)

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.caption("Uber Trip Analytics • Trip Analysis")