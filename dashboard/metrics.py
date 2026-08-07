import streamlit as st


def show_metrics(df):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🚖 Total Trips",
        f"{int(df['total_trips'][0]):,}"
    )

    col2.metric(
        "💰 Revenue",
        f"${float(df['total_revenue'][0]):,.2f}"
    )

    col3.metric(
        "💵 Avg Fare",
        f"${float(df['average_fare'][0]):.2f}"
    )

    col4.metric(
        "📏 Avg Distance",
        f"{float(df['average_distance'][0]):.2f} mi"
    )