import streamlit as st
import pandas as pd
import plotly.express as px

from db_connection import run_query

st.set_page_config(
    page_title="Revenue Analysis",
    page_icon="💰",
    layout="wide"
)

PRIMARY = "#2F7D7A"
SECONDARY = "#64748B"

st.title("💰 Revenue Analysis")
st.markdown("Analyze trip revenue, fares, tips and driver earnings.")
st.divider()

KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,
    COALESCE(ROUND(SUM(total_revenue)::numeric, 2), 0) AS total_revenue,
    COALESCE(ROUND(AVG(total_revenue)::numeric, 2), 0) AS avg_trip_value,
    COALESCE(ROUND(SUM(tips)::numeric, 2), 0) AS total_tips,
    COALESCE(ROUND(SUM(driver_pay)::numeric, 2), 0) AS total_driver_pay
FROM warehouse.fact_trips;
"""

kpi_df = run_query(KPI_QUERY)

if not kpi_df.empty:
    row = kpi_df.iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Revenue",
        f"${float(row['total_revenue']):,.2f}"
    )

    col2.metric(
        "💵 Avg Trip Value",
        f"${float(row['avg_trip_value']):,.2f}"
    )

    col3.metric(
        "💡 Total Tips",
        f"${float(row['total_tips']):,.2f}"
    )

    col4.metric(
        "👨‍✈️ Driver Pay",
        f"${float(row['total_driver_pay']):,.2f}"
    )

st.divider()

st.subheader("Revenue by Hour")

HOURLY_REVENUE_QUERY = """
SELECT
    pickup_hour,
    ROUND(SUM(total_revenue)::numeric, 2) AS total_revenue
FROM warehouse.fact_trips
WHERE pickup_hour IS NOT NULL
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

hourly_revenue_df = run_query(HOURLY_REVENUE_QUERY)

if not hourly_revenue_df.empty:
    hourly_revenue_df["pickup_hour"] = (
        hourly_revenue_df["pickup_hour"].astype(int)
    )

    fig = px.line(
        hourly_revenue_df,
        x="pickup_hour",
        y="total_revenue",
        markers=True,
        labels={
            "pickup_hour": "Pickup Hour",
            "total_revenue": "Revenue ($)"
        }
    )

    fig.update_traces(
        line=dict(color=PRIMARY, width=3),
        marker=dict(color=PRIMARY, size=7)
    )

    fig.update_layout(
        template="simple_white",
        height=400,
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Trip Value Distribution")

FARE_QUERY = """
SELECT
    total_revenue
FROM warehouse.fact_trips
WHERE total_revenue IS NOT NULL
AND total_revenue >= 0;
"""

fare_df = run_query(FARE_QUERY)

if not fare_df.empty:
    fare_df["total_revenue"] = pd.to_numeric(
        fare_df["total_revenue"],
        errors="coerce"
    )

    fare_df = fare_df.dropna()

    fig = px.histogram(
        fare_df,
        x="total_revenue",
        nbins=30,
        labels={
            "total_revenue": "Trip Value ($)"
        }
    )

    fig.update_traces(marker_color=PRIMARY)

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Trip Distance vs Revenue")

DISTANCE_QUERY = """
SELECT
    trip_miles,
    total_revenue
FROM warehouse.fact_trips
WHERE trip_miles IS NOT NULL
AND total_revenue IS NOT NULL
AND trip_miles >= 0
AND total_revenue >= 0;
"""

distance_df = run_query(DISTANCE_QUERY)

if not distance_df.empty:
    distance_df["trip_miles"] = pd.to_numeric(
        distance_df["trip_miles"],
        errors="coerce"
    )

    distance_df["total_revenue"] = pd.to_numeric(
        distance_df["total_revenue"],
        errors="coerce"
    )

    distance_df = distance_df.dropna()

    fig = px.scatter(
        distance_df,
        x="trip_miles",
        y="total_revenue",
        labels={
            "trip_miles": "Trip Distance (miles)",
            "total_revenue": "Revenue ($)"
        },
        opacity=0.65
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

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Revenue Components")

COMPONENT_QUERY = """
SELECT
    ROUND(SUM(base_passenger_fare)::numeric, 2) AS base_fare,
    ROUND(SUM(tolls)::numeric, 2) AS tolls,
    ROUND(SUM(tips)::numeric, 2) AS tips,
    ROUND(SUM(congestion_surcharge)::numeric, 2) AS congestion_surcharge,
    ROUND(SUM(airport_fee)::numeric, 2) AS airport_fee
FROM warehouse.fact_trips;
"""

component_df = run_query(COMPONENT_QUERY)

if not component_df.empty:
    component_df = component_df.T.reset_index()

    component_df.columns = [
        "component",
        "amount"
    ]

    component_df["amount"] = pd.to_numeric(
        component_df["amount"],
        errors="coerce"
    )

    fig = px.bar(
        component_df,
        x="component",
        y="amount",
        labels={
            "component": "Revenue Component",
            "amount": "Amount ($)"
        }
    )

    fig.update_traces(marker_color=SECONDARY)

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Driver Pay vs Trip Revenue")

DRIVER_QUERY = """
SELECT
    ROUND(SUM(total_revenue)::numeric, 2) AS total_revenue,
    ROUND(SUM(driver_pay)::numeric, 2) AS driver_pay
FROM warehouse.fact_trips;
"""

driver_df = run_query(DRIVER_QUERY)

if not driver_df.empty:
    chart_df = pd.DataFrame({
        "Metric": [
            "Trip Revenue",
            "Driver Pay"
        ],
        "Amount": [
            float(driver_df.iloc[0]["total_revenue"]),
            float(driver_df.iloc[0]["driver_pay"])
        ]
    })

    fig = px.bar(
        chart_df,
        x="Metric",
        y="Amount",
        labels={
            "Metric": "",
            "Amount": "Amount ($)"
        }
    )

    fig.update_traces(marker_color=PRIMARY)

    fig.update_layout(
        template="simple_white",
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.caption("Uber Trip Analytics • Revenue Analysis")