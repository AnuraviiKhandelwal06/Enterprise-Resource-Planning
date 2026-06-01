import streamlit as st
import pandas as pd
import requests

st.title("View Products")
try:
    response = requests.get(
        "http://127.0.0.1:8000/products"
    )
    if response.status_code == 200:
        products = response.json()
        search = st.text_input(
            "Search Product"
        )
        if search:
            products = [
                p for p in products
                if search.lower()
                in p["name"].lower()
            ]
        df = pd.DataFrame(products)
        st.dataframe(
            df,
            use_container_width=True
        )
    else:
        st.error(
            "Failed to fetch products"
        )

except Exception as e:
    st.error(
        f"Connection Error: {e}"
    )