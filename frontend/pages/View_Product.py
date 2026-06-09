import streamlit as st
import pandas as pd
import requests

st.title("View Products")

token = st.session_state.get("token")

if not token:
    st.error("Please login first")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

try:
    response = requests.get(
        "http://127.0.0.1:8000/products",
        headers=headers
    )

    if response.status_code == 200:
        products = response.json()

        search = st.text_input("Search Product")

        if search:
            products = [
                p for p in products
                if search.lower() in p["name"].lower()
            ]

        df = pd.DataFrame(products)

        st.dataframe(
            df,
            use_container_width=True
        )

    elif response.status_code == 401:
        st.error("Unauthorized — please login again")
        st.session_state.token = None
        st.rerun()

    else:
        st.error("Failed to fetch products")

except Exception as e:
    st.error(f"Connection Error: {e}")