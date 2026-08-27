import streamlit as st
import pandas as pd
import plotly.express as px

from db_connection import run_query

st.set_page_config(
    page_title="Location Analysis",
    page_icon="📍",
    layout="wide"
)

PRIMARY = "#2F7D7A"
SECONDARY = "#64748B"

st.title("📍 Location Analysis")
st.markdown("Analyze pickup zones, drop-off zones and the most frequent trip routes.")
st.divider()

PICKUP_QUERY = """
SELECT
    pickup_location,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_location IS NOT NULL
GROUP BY pickup_location
ORDER BY total_trips DESC
LIMIT 10;
"""

DROPOFF_QUERY = """
SELECT
    dropoff_location,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE dropoff_location IS NOT NULL
GROUP BY dropoff_location
ORDER BY total_trips DESC
LIMIT 10;
"""

ROUTE_QUERY = """
SELECT
    pickup_location,
    dropoff_location,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_location IS NOT NULL
AND dropoff_location IS NOT NULL
GROUP BY pickup_location, dropoff_location
ORDER BY total_trips DESC
LIMIT 15;
"""

UNIQUE_PICKUP_QUERY = """
SELECT COUNT(DISTINCT pickup_location) AS unique_pickup_zones
FROM warehouse.fact_trips
WHERE pickup_location IS NOT NULL;
"""

UNIQUE_DROPOFF_QUERY = """
SELECT COUNT(DISTINCT dropoff_location) AS unique_dropoff_zones
FROM warehouse.fact_trips
WHERE dropoff_location IS NOT NULL;
"""

TOTAL_ROUTES_QUERY = """
SELECT COUNT(DISTINCT (pickup_location, dropoff_location)) AS unique_routes
FROM warehouse.fact_trips
WHERE pickup_location IS NOT NULL
AND dropoff_location IS NOT NULL;
"""

pickup_df = run_query(PICKUP_QUERY)
dropoff_df = run_query(DROPOFF_QUERY)
route_df = run_query(ROUTE_QUERY)
pickup_count_df = run_query(UNIQUE_PICKUP_QUERY)
dropoff_count_df = run_query(UNIQUE_DROPOFF_QUERY)
route_count_df = run_query(TOTAL_ROUTES_QUERY)

col1, col2, col3 = st.columns(3)

if not pickup_count_df.empty:
    col1.metric(
        "📍 Pickup Zones",
        f"{int(pickup_count_df.iloc[0]['unique_pickup_zones']):,}"
    )

if not dropoff_count_df.empty:
    col2.metric(
        "📍 Drop-off Zones",
        f"{int(dropoff_count_df.iloc[0]['unique_dropoff_zones']):,}"
    )

if not route_count_df.empty:
    col3.metric(
        "🛣️ Unique Routes",
        f"{int(route_count_df.iloc[0]['unique_routes']):,}"
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("Top Pickup Locations")

    if not pickup_df.empty:

        pickup_df["pickup_location"] = (
            pickup_df["pickup_location"].astype(str)
        )

        fig = px.bar(
            pickup_df.sort_values("total_trips"),
            x="total_trips",
            y="pickup_location",
            orientation="h",
            labels={
                "pickup_location": "Pickup Zone",
                "total_trips": "Trips"
            }
        )

        fig.update_traces(marker_color=PRIMARY)

        fig.update_layout(
            template="simple_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    st.subheader("Top Drop-off Locations")

    if not dropoff_df.empty:

        dropoff_df["dropoff_location"] = (
            dropoff_df["dropoff_location"].astype(str)
        )

        fig = px.bar(
            dropoff_df.sort_values("total_trips"),
            x="total_trips",
            y="dropoff_location",
            orientation="h",
            labels={
                "dropoff_location": "Drop-off Zone",
                "total_trips": "Trips"
            }
        )

        fig.update_traces(marker_color=SECONDARY)

        fig.update_layout(
            template="simple_white",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.subheader("🛣️ Most Frequent Routes")

if not route_df.empty:

    route_df["route"] = (
        route_df["pickup_location"].astype(str)
        + " → "
        + route_df["dropoff_location"].astype(str)
    )

    route_df = route_df.sort_values(
        "total_trips",
        ascending=True
    )

    fig = px.bar(
        route_df,
        x="total_trips",
        y="route",
        orientation="h",
        labels={
            "route": "Route",
            "total_trips": "Trips"
        }
    )

    fig.update_traces(marker_color=PRIMARY)

    fig.update_layout(
        template="simple_white",
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("Route Details")

if not route_df.empty:

    display_df = route_df[
        [
            "pickup_location",
            "dropoff_location",
            "total_trips"
        ]
    ].copy()

    display_df.columns = [
        "Pickup Zone",
        "Drop-off Zone",
        "Total Trips"
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.caption("Uber Trip Analytics • Location Analysis")