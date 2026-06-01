import streamlit as st
import requests

st.title("Sell Product")

with st.form("sell_form"):
    item_name = st.text_input("Product Name")
    quantity = st.number_input(
        "Quantity",
        min_value=1,
        step=1
    )
    selling_price = st.number_input(
        "Selling Price",
        min_value=0,
        step=1
    )
    submit = st.form_submit_button("Sell Product")

if submit:
    if not item_name.strip():
        st.warning("Please enter a product name")
    else:
        payload = {
            "item_name": item_name,
            "quantity": int(quantity),
            "selling_price": int(selling_price)
        }
        try:
            response = requests.put(
                "http://127.0.0.1:8000/products/sell",
                json=payload
            )
            st.write("Status Code:", response.status_code)
            st.write("Raw Response:", response.text)

            try:
                data = response.json()
            except Exception:
                st.error("Backend did not return valid JSON")
                st.stop()

            if response.status_code == 200:
                st.success("Product sold successfully")
                st.json(data)
            else:
                st.error(data.get("detail") or data.get("message") or "Something went wrong")

        except Exception as e:
            st.error(f"Connection Error: {e}")