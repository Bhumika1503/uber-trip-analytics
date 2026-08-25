import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


COLORS = {
    "navy": "#264653",
    "teal": "#2A9D8F",
    "blue": "#457B9D",
    "purple": "#6C63A8",
    "gold": "#E9C46A",
    "coral": "#E76F51",
    "light": "#F4F6F8"
}


def apply_layout(fig, height=420):

    fig.update_layout(
        height=height,
        template="plotly_white",
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=40
        ),
        font=dict(
            family="Arial",
            size=13
        ),
        title_font=dict(
            size=18
        ),
        hovermode="x unified"
    )

    return fig


# ============================================================
# PAYMENT REVENUE
# ============================================================

def payment_revenue_chart(df):

    if df.empty:
        return

    fig = px.bar(
        df,
        x="payment_method",
        y="revenue",
        text="revenue",
        title="Revenue by Payment Method"
    )

    fig.update_traces(
        marker_color=COLORS["teal"],
        texttemplate="$%{text:,.0f}",
        textposition="outside"
    )

    fig.update_yaxes(
        title="Revenue ($)"
    )

    fig.update_xaxes(
        title=""
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAYMENT DONUT
# ============================================================

def payment_donut_chart(df):

    if df.empty:
        return

    fig = px.pie(
        df,
        names="payment_method",
        values="revenue",
        hole=0.55,
        title="Revenue Share by Payment Method"
    )

    fig.update_traces(
        marker=dict(
            colors=[
                COLORS["teal"],
                COLORS["blue"],
                COLORS["gold"],
                COLORS["coral"],
                COLORS["purple"]
            ]
        ),
        textposition="inside",
        textinfo="percent+label"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# VENDOR PERFORMANCE
# ============================================================

def vendor_performance_chart(df):

    if df.empty:
        return

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=df["vendor_id"],
            y=df["trips"],
            name="Trips",
            marker_color=COLORS["blue"]
        )
    )

    fig.add_trace(
        go.Bar(
            x=df["vendor_id"],
            y=df["revenue"],
            name="Revenue",
            marker_color=COLORS["teal"],
            yaxis="y2"
        )
    )

    fig.update_layout(
        title="Vendor Performance",
        xaxis_title="Vendor",
        yaxis=dict(
            title="Trips"
        ),
        yaxis2=dict(
            title="Revenue ($)",
            overlaying="y",
            side="right"
        ),
        barmode="group"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# AVERAGE FARE BY VENDOR
# ============================================================

def vendor_fare_chart(df):

    if df.empty:
        return

    fig = px.bar(
        df,
        x="vendor_id",
        y="average_fare",
        text="average_fare",
        title="Average Fare by Vendor"
    )

    fig.update_traces(
        marker_color=COLORS["purple"],
        texttemplate="$%{text:.2f}",
        textposition="outside"
    )

    fig.update_xaxes(
        title="Vendor"
    )

    fig.update_yaxes(
        title="Average Fare ($)"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# DISTANCE BY VENDOR
# ============================================================

def vendor_distance_chart(df):

    if df.empty:
        return

    fig = px.bar(
        df,
        x="vendor_id",
        y="average_distance",
        text="average_distance",
        title="Average Trip Distance by Vendor"
    )

    fig.update_traces(
        marker_color=COLORS["gold"],
        texttemplate="%{text:.2f} mi",
        textposition="outside"
    )

    fig.update_xaxes(
        title="Vendor"
    )

    fig.update_yaxes(
        title="Distance (miles)"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# DISTANCE DISTRIBUTION
# ============================================================

def distance_distribution(df):

    if df.empty:
        return

    fig = px.histogram(
        df,
        x="trip_distance",
        nbins=40,
        title="Trip Distance Distribution"
    )

    fig.update_traces(
        marker_color=COLORS["blue"]
    )

    fig.update_xaxes(
        title="Trip Distance (miles)"
    )

    fig.update_yaxes(
        title="Number of Trips"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# FARE DISTRIBUTION
# ============================================================

def fare_distribution(df):

    if df.empty:
        return

    fig = px.histogram(
        df,
        x="fare_amount",
        nbins=40,
        title="Fare Distribution"
    )

    fig.update_traces(
        marker_color=COLORS["coral"]
    )

    fig.update_xaxes(
        title="Fare ($)"
    )

    fig.update_yaxes(
        title="Number of Trips"
    )

    apply_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# DISTANCE VS FARE
# ============================================================

def distance_fare_scatter(df):

    if df.empty:
        return

    fig = px.scatter(
        df,
        x="trip_distance",
        y="total_amount",
        opacity=0.35,
        title="Trip Distance vs Total Fare",
        labels={
            "trip_distance": "Trip Distance (miles)",
            "total_amount": "Total Fare ($)"
        }
    )

    fig.update_traces(
        marker=dict(
            color=COLORS["teal"],
            size=5
        )
    )

    apply_layout(fig, 450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# TOP PICKUP LOCATIONS
# ============================================================

def pickup_location_chart(df):

    if df.empty:
        return

    df = df.sort_values("trips")

    fig = px.bar(
        df,
        x="trips",
        y="pickup_location",
        orientation="h",
        text="trips",
        title="Top 10 Pickup Locations"
    )

    fig.update_traces(
        marker_color=COLORS["navy"],
        textposition="outside"
    )

    fig.update_xaxes(
        title="Number of Trips"
    )

    fig.update_yaxes(
        title=""
    )

    apply_layout(fig, 500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# TOP ROUTES
# ============================================================

def top_routes_chart(df):

    if df.empty:
        return

    df = df.sort_values("trips")

    fig = px.bar(
        df,
        x="trips",
        y="route",
        orientation="h",
        text="trips",
        title="Top 10 Trip Routes"
    )

    fig.update_traces(
        marker_color=COLORS["purple"],
        textposition="outside"
    )

    fig.update_xaxes(
        title="Number of Trips"
    )

    fig.update_yaxes(
        title=""
    )

    apply_layout(fig, 500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )