import streamlit as st
import requests

st.title("Delete Product")

product_name = st.text_input("Enter Product Name")

if st.button("Delete Product"):

    if not product_name.strip():
        st.warning("Please enter a product name")
        st.stop()

    try:
        response = requests.put(
            f"http://127.0.0.1:8000/products/{product_name}"
        )
        st.write("Status Code:", response.status_code)

        try:
            data = response.json()
        except Exception:
            st.error("Backend did not return valid JSON")
            st.write("Raw Response:", response.text)
            st.stop()

        if response.status_code == 200:
            st.success("✅ Product soft deleted successfully")
            st.json(data)
        else:
            st.error(
                data.get("detail", data.get("message", "Something went wrong"))
            )

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")