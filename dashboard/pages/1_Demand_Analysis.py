import streamlit as st
import pandas as pd
import plotly.express as px

from db_connection import run_query


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Demand Analysis",
    page_icon="📈",
    layout="wide"
)


# =========================================================
# PROFESSIONAL PALETTE
# =========================================================

PRIMARY = "#2F7D7A"
SECONDARY = "#64748B"
DARK = "#1F2937"
LIGHT = "#F8FAFC"


# =========================================================
# PAGE HEADER
# =========================================================

st.title("📈 Demand Analysis")

st.markdown(
    "Understand when Uber demand is highest and identify "
    "the busiest periods."
)

st.divider()


# =========================================================
# LOAD DATA
# =========================================================

HOUR_QUERY = """
SELECT
    pickup_hour,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_hour IS NOT NULL
GROUP BY pickup_hour
ORDER BY pickup_hour;
"""

DAY_QUERY = """
SELECT
    pickup_day,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_day IS NOT NULL
GROUP BY pickup_day
ORDER BY total_trips DESC;
"""

HEATMAP_QUERY = """
SELECT
    pickup_day,
    pickup_hour,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_day IS NOT NULL
  AND pickup_hour IS NOT NULL
GROUP BY pickup_day, pickup_hour
ORDER BY pickup_day, pickup_hour;
"""

COMPARISON_QUERY = """
SELECT
    CASE
        WHEN pickup_day IN ('Saturday', 'Sunday')
        THEN 'Weekend'
        ELSE 'Weekday'
    END AS period,
    COUNT(*) AS total_trips
FROM warehouse.fact_trips
WHERE pickup_day IS NOT NULL
GROUP BY period
ORDER BY total_trips DESC;
"""


hour_df = run_query(HOUR_QUERY)
day_df = run_query(DAY_QUERY)
heatmap_df = run_query(HEATMAP_QUERY)
comparison_df = run_query(COMPARISON_QUERY)


# =========================================================
# KPI CALCULATIONS
# =========================================================

if not hour_df.empty:

    peak_hour_row = hour_df.loc[
        hour_df["total_trips"].idxmax()
    ]

    peak_hour = int(peak_hour_row["pickup_hour"])
    peak_hour_trips = int(
        peak_hour_row["total_trips"]
    )

else:

    peak_hour = 0
    peak_hour_trips = 0


if not day_df.empty:

    peak_day_row = day_df.iloc[0]

    peak_day = peak_day_row["pickup_day"]
    peak_day_trips = int(
        peak_day_row["total_trips"]
    )

else:

    peak_day = "N/A"
    peak_day_trips = 0


# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "🔥 Peak Hour",
    f"{peak_hour}:00",
    f"{peak_hour_trips:,} trips"
)

col2.metric(
    "📅 Busiest Day",
    peak_day,
    f"{peak_day_trips:,} trips"
)

if not hour_df.empty:

    average_hourly_trips = hour_df[
        "total_trips"
    ].mean()

else:

    average_hourly_trips = 0


col3.metric(
    "📊 Avg Hourly Trips",
    f"{average_hourly_trips:,.0f}"
)


st.divider()


# =========================================================
# TRIPS BY HOUR
# =========================================================

st.subheader("Trips by Hour")

if not hour_df.empty:

    hour_df["pickup_hour"] = (
        hour_df["pickup_hour"].astype(int)
    )

    fig_hour = px.line(
        hour_df,
        x="pickup_hour",
        y="total_trips",
        markers=True,
        labels={
            "pickup_hour": "Pickup Hour",
            "total_trips": "Number of Trips"
        }
    )

    fig_hour.update_traces(
        line=dict(color=PRIMARY, width=3),
        marker=dict(color=PRIMARY, size=7)
    )

    fig_hour.update_layout(
        template="simple_white",
        height=400,
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig_hour,
        use_container_width=True
    )

else:

    st.info("No hourly demand data available.")


# =========================================================
# TRIPS BY DAY
# =========================================================

st.subheader("Trips by Day of Week")

if not day_df.empty:

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    day_df["pickup_day"] = pd.Categorical(
        day_df["pickup_day"],
        categories=day_order,
        ordered=True
    )

    day_df = day_df.sort_values("pickup_day")

    fig_day = px.bar(
        day_df,
        x="pickup_day",
        y="total_trips",
        labels={
            "pickup_day": "Day",
            "total_trips": "Number of Trips"
        }
    )

    fig_day.update_traces(
        marker_color=PRIMARY
    )

    fig_day.update_layout(
        template="simple_white",
        height=400,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig_day,
        use_container_width=True
    )

else:

    st.info("No daily demand data available.")


# =========================================================
# DEMAND HEATMAP
# =========================================================

st.subheader("Demand Heatmap")

st.caption(
    "Shows how trip demand changes across hours and days."
)

if not heatmap_df.empty:

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    heatmap_df["pickup_day"] = pd.Categorical(
        heatmap_df["pickup_day"],
        categories=day_order,
        ordered=True
    )

    heatmap_df = heatmap_df.sort_values(
        ["pickup_day", "pickup_hour"]
    )

    pivot_df = heatmap_df.pivot(
        index="pickup_day",
        columns="pickup_hour",
        values="total_trips"
    )

    fig_heatmap = px.imshow(
        pivot_df,
        labels={
            "x": "Pickup Hour",
            "y": "Day",
            "color": "Trips"
        },
        aspect="auto",
        color_continuous_scale=[
            "#E6F2F1",
            "#2F7D7A"
        ]
    )

    fig_heatmap.update_layout(
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig_heatmap,
        use_container_width=True
    )

else:

    st.info("No heatmap data available.")


# =========================================================
# WEEKDAY VS WEEKEND
# =========================================================

st.subheader("Weekday vs Weekend")

if not comparison_df.empty:

    fig_comparison = px.bar(
        comparison_df,
        x="period",
        y="total_trips",
        labels={
            "period": "",
            "total_trips": "Number of Trips"
        }
    )

    fig_comparison.update_traces(
        marker_color=SECONDARY
    )

    fig_comparison.update_layout(
        template="simple_white",
        height=350,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    st.plotly_chart(
        fig_comparison,
        use_container_width=True
    )

else:

    st.info(
        "No weekday/weekend data available."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Uber Trip Analytics • Demand Analysis"
)