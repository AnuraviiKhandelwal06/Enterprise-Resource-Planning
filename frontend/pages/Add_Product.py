import streamlit as st
import requests

st.title("Add Product")

with st.form("add_product"):
    name = st.text_input("Product Name")
    price = st.number_input(
        "Price",
        min_value=0,
        step=1
    )
    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )
    submit = st.form_submit_button(
        "Add Product"
    )

if submit:
    if not name.strip():
        st.warning("Please enter a product name.")
    else:
        payload = {
            "name": name,
            "price": int(price),
            "quantity": int(quantity)
        }
        try:
            response = requests.post(
               "http://127.0.0.1:8000/products",
                json=payload
            )
            st.write("Status Code:", response.status_code)
            st.write("Response Text:", response.text)

        except Exception as e:
            st.error(f"Error: {e}")