import streamlit as st
import requests

st.title("Signup")

BASE_URL = "http://127.0.0.1:8000"

with st.form("signup_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Create Account")

if submit:

    if not username.strip():
        st.warning("Please enter a username")
        st.stop()

    if not password:
        st.warning("Please enter a password")
        st.stop()

    if password != confirm_password:
        st.error("Passwords do not match")
        st.stop()

    payload = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(
            f"{BASE_URL}/signup",
            json=payload
        )

        if response.status_code == 200 or response.status_code == 201:
            st.success("Account created successfully! You can now login.")
            st.json(response.json())

        else:
            try:
                st.error(response.json().get("detail", "Signup failed"))
            except:
                st.error(response.text)

    except Exception as e:
        st.error(f"Connection Error: {e}")