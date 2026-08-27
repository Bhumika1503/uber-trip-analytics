import streamlit as st
import pandas as pd
import plotly.express as px

from db_connection import run_query

st.set_page_config(
    page_title="Ride Type Analysis",
    page_icon="🤝",
    layout="wide"
)

PRIMARY = "#2F7D7A"
SECONDARY = "#64748B"

st.title("🤝 Ride Type Analysis")
st.markdown("Analyze shared rides and wheelchair-accessible ride requests.")
st.divider()

KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,

    SUM(
        CASE
            WHEN shared_request_flag = 'Y'
            THEN 1 ELSE 0
        END
    ) AS shared_requests,

    SUM(
        CASE
            WHEN shared_match_flag = 'Y'
            THEN 1 ELSE 0
        END
    ) AS shared_matches,

    SUM(
        CASE
            WHEN wav_request_flag = 'Y'
            THEN 1 ELSE 0
        END
    ) AS wav_requests,

    SUM(
        CASE
            WHEN wav_match_flag = 'Y'
            THEN 1 ELSE 0
        END
    ) AS wav_matches

FROM warehouse.fact_trips;
"""

kpi_df = run_query(KPI_QUERY)

if not kpi_df.empty:

    row = kpi_df.iloc[0]

    total_trips = int(row["total_trips"])
    shared_requests = int(row["shared_requests"])
    shared_matches = int(row["shared_matches"])
    wav_requests = int(row["wav_requests"])
    wav_matches = int(row["wav_matches"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🤝 Shared Requests",
        f"{shared_requests:,}"
    )

    col2.metric(
        "✅ Shared Matches",
        f"{shared_matches:,}"
    )

    col3.metric(
        "♿ WAV Requests",
        f"{wav_requests:,}"
    )

    col4.metric(
        "♿ WAV Matches",
        f"{wav_matches:,}"
    )

st.divider()

st.subheader("Shared Ride Activity")

SHARED_QUERY = """
SELECT
    'Shared Requests' AS ride_type,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE shared_request_flag = 'Y'

UNION ALL

SELECT
    'Shared Matches' AS ride_type,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE shared_match_flag = 'Y'

ORDER BY total_trips DESC;
"""

shared_df = run_query(SHARED_QUERY)

if not shared_df.empty:

    fig = px.bar(
        shared_df,
        x="ride_type",
        y="total_trips",
        labels={
            "ride_type": "",
            "total_trips": "Trips"
        }
    )

    fig.update_traces(
        marker_color=PRIMARY
    )

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("WAV Accessibility Activity")

WAV_QUERY = """
SELECT
    'WAV Requests' AS ride_type,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE wav_request_flag = 'Y'

UNION ALL

SELECT
    'WAV Matches' AS ride_type,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE wav_match_flag = 'Y'

ORDER BY total_trips DESC;
"""

wav_df = run_query(WAV_QUERY)

if not wav_df.empty:

    fig = px.bar(
        wav_df,
        x="ride_type",
        y="total_trips",
        labels={
            "ride_type": "",
            "total_trips": "Trips"
        }
    )

    fig.update_traces(
        marker_color=SECONDARY
    )

    fig.update_layout(
        template="simple_white",
        height=400
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.subheader("Shared Ride Match Rate")

if not kpi_df.empty:

    match_rate = (
        shared_matches / shared_requests * 100
        if shared_requests > 0
        else 0
    )

    st.metric(
        "Shared Match Rate",
        f"{match_rate:.2f}%"
    )

st.subheader("WAV Match Rate")

if not kpi_df.empty:

    wav_match_rate = (
        wav_matches / wav_requests * 100
        if wav_requests > 0
        else 0
    )

    st.metric(
        "WAV Match Rate",
        f"{wav_match_rate:.2f}%"
    )

st.divider()

st.caption("Uber Trip Analytics • Ride Type Analysis")