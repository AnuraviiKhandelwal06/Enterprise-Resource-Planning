import streamlit as st
import pandas as pd

token = st.session_state.get("token")

if not token:
    st.error("Please login first")
    st.stop()

st.title("Analytics Dashboard")

sales = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],
    "Revenue": [
        10000,
        15000,
        20000,
        25000,
        30000
    ]
})

col1, col2 = st.columns(2)
with col1:
    st.subheader("Revenue Trend")
    st.line_chart(
        sales.set_index("Month")
    )
with col2:
    st.subheader("Revenue Comparison")
    st.bar_chart(
        sales.set_index("Month")
    )
st.divider()

st.metric(
    label="Total Revenue",
    value=f"₹{sales['Revenue'].sum():,}"
)