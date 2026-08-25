import streamlit as st

from db_connection import run_query

from queries import (
    KPI_QUERY,
    PAYMENT_QUERY,
    VENDOR_QUERY,
    TOP_PICKUP_QUERY,
    TOP_ROUTES_QUERY,
    DISTANCE_QUERY,
    FARE_QUERY,
    DISTANCE_FARE_QUERY
)

from charts import (
    payment_revenue_chart,
    payment_donut_chart,
    vendor_performance_chart,
    vendor_fare_chart,
    vendor_distance_chart,
    distance_distribution,
    fare_distribution,
    distance_fare_scatter,
    pickup_location_chart,
    top_routes_chart
)


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Uber Trip Analytics",
    page_icon="🚖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #F8FAFC;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        color: #264653;
    }

    h2, h3 {
        color: #264653;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🚖 Uber Analytics")

st.sidebar.markdown(
    "### Navigation"
)

page = st.sidebar.radio(
    "",
    [
        "Dashboard",
        "About"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title("Uber Trip Analytics")

    st.markdown(
        "### End-to-End Data Engineering & Business Intelligence"
    )

    st.caption(
        "Interactive analysis of Uber trip data using PostgreSQL and Streamlit"
    )

    st.divider()


    # ========================================================
    # KPI
    # ========================================================

    kpi_df = run_query(KPI_QUERY)

    if not kpi_df.empty:

        row = kpi_df.iloc[0]

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Total Trips",
            f"{int(row['total_trips']):,}"
        )

        col2.metric(
            "Total Revenue",
            f"${float(row['total_revenue']):,.2f}"
        )

        col3.metric(
            "Average Fare",
            f"${float(row['average_fare']):,.2f}"
        )

        col4.metric(
            "Average Distance",
            f"{float(row['average_distance']):,.2f} mi"
        )

        col5.metric(
            "Avg Passengers",
            f"{float(row['average_passengers']):,.2f}"
        )


    st.divider()


    # ========================================================
    # PAYMENT ANALYSIS
    # ========================================================

    payment_df = run_query(PAYMENT_QUERY)

    col1, col2 = st.columns(2)

    with col1:

        payment_revenue_chart(payment_df)

    with col2:

        payment_donut_chart(payment_df)


    st.divider()


    # ========================================================
    # VENDOR ANALYSIS
    # ========================================================

    vendor_df = run_query(VENDOR_QUERY)

    col1, col2 = st.columns(2)

    with col1:

        vendor_performance_chart(vendor_df)

    with col2:

        vendor_fare_chart(vendor_df)


    col1, col2 = st.columns(2)

    with col1:

        vendor_distance_chart(vendor_df)

    with col2:

        st.subheader("Vendor Analysis")

        st.dataframe(
            vendor_df,
            use_container_width=True,
            hide_index=True
        )


    st.divider()


    # ========================================================
    # TRIP BEHAVIOR
    # ========================================================

    st.header("Trip Behavior")

    distance_df = run_query(DISTANCE_QUERY)

    fare_df = run_query(FARE_QUERY)

    distance_fare_df = run_query(DISTANCE_FARE_QUERY)


    col1, col2 = st.columns(2)

    with col1:

        distance_distribution(distance_df)

    with col2:

        fare_distribution(fare_df)


    distance_fare_scatter(
        distance_fare_df
    )


    st.divider()


    # ========================================================
    # LOCATION ANALYSIS
    # ========================================================

    st.header("Location & Route Analysis")

    pickup_df = run_query(
        TOP_PICKUP_QUERY
    )

    route_df = run_query(
        TOP_ROUTES_QUERY
    )


    col1, col2 = st.columns(2)

    with col1:

        pickup_location_chart(
            pickup_df
        )

    with col2:

        top_routes_chart(
            route_df
        )


# ============================================================
# ABOUT
# ============================================================

else:

    st.title("About This Project")

    st.markdown(
        """
        ## Uber Trip Analytics Pipeline

        This is an end-to-end data engineering project that
        transforms raw Uber trip data into analytical insights.

        ### Architecture

        **Raw Data**

        ↓

        **Python ETL**

        ↓

        **Validation & Transformation**

        ↓

        **PostgreSQL Data Warehouse**

        ↓

        **Apache Spark Analytics**

        ↓

        **Streamlit Dashboard**

        ### Technology Stack

        - Python
        - Pandas
        - PostgreSQL
        - SQL
        - Apache Spark
        - JDBC
        - Streamlit
        - Plotly

        ### Dashboard Analysis

        - Revenue analysis
        - Payment behavior
        - Vendor performance
        - Fare analysis
        - Trip distance analysis
        - Distance vs fare relationship
        - Pickup location analysis
        - Popular route analysis
        """
    )