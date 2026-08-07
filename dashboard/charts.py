import streamlit as st


def payment_chart(df):

    st.subheader("💳 Revenue by Payment Method")

    st.bar_chart(
        df,
        x="payment_method",
        y="revenue"
    )


def vendor_chart(df):

    st.subheader("🚕 Trips by Vendor")

    st.bar_chart(
        df,
        x="vendor_id",
        y="trips"
    )


def distance_chart(df):

    st.subheader("📏 Average Trip Distance")

    st.bar_chart(
        df,
        x="vendor_id",
        y="avg_distance"
    )