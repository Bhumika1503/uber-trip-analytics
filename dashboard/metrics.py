import streamlit as st


def show_metrics(df):

    if df.empty:
        st.warning("No data available.")
        return

    row = df.iloc[0]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "🚖 Total Trips",
        f"{int(row['total_trips']):,}"
    )

    col2.metric(
        "💰 Total Revenue",
        f"${float(row['total_revenue']):,.2f}"
    )

    col3.metric(
        "💵 Average Fare",
        f"${float(row['average_fare']):,.2f}"
    )

    col4.metric(
        "📏 Average Distance",
        f"{float(row['average_distance']):,.2f} mi"
    )

    if "average_passengers" in row.index:
        col5.metric(
            "👥 Avg Passengers",
            f"{float(row['average_passengers']):,.2f}"
        )
    else:
        col5.metric(
            "👥 Avg Passengers",
            "N/A"
        )