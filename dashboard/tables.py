import streamlit as st


def pickup_table(df):

    st.subheader("📍 Top Pickup Locations")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )