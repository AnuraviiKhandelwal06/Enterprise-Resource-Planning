import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ERP Dashboard",
    layout="wide"
)

st.title("ERP Management System")
st.caption("Inventory Management Dashboard")

with st.sidebar:
    st.title("ERP Menu")
    st.success("Backend Connected")
    st.info("Use the pages below to manage products.")

st.subheader("Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Products",
        value=120
    )

with col2:
    st.metric(
        label="Sales",
        value=250
    )

with col3:
    st.metric(
        label="Revenue",
        value="₹50,000"
    )

with col4:
    st.metric(
        label="Low Stock",
        value=12
    )
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Monthly Sales")
    sales_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [1000, 1500, 1200, 2000, 2500]
    })
    st.line_chart(
        sales_data.set_index("Month")
    )

with col2:
    st.subheader("Inventory Trend")
    inventory_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Stock": [500, 450, 420, 380, 350]
    })
    st.bar_chart(
        inventory_data.set_index("Month")
    )

st.divider()
