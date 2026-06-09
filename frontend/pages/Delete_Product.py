import streamlit as st
import requests

st.title("Delete Product (Soft Delete)")

token = st.session_state.get("token")

if not token:
    st.error("Please login first")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

product_name = st.text_input("Enter Product Name")

if st.button("Delete Product"):
    if not product_name.strip():
        st.warning("Please enter a product name")
        st.stop()
    try:
        response = requests.put(
            f"http://127.0.0.1:8000/products/{product_name}",
            headers=headers
        )
        if response.status_code == 200:
            st.success("Product soft deleted successfully")
            st.json(response.json())
        else:
            try:
                st.error(response.json())
            except:
                st.error(response.text)

    except Exception as e:
        st.error(f"Error: {e}")