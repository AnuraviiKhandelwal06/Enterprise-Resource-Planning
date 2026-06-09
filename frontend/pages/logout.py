import streamlit as st

st.title("Logout")

if st.session_state.get("token"):
    st.warning("Are you sure you want to logout?")
    if st.button("Logout"):
        st.session_state.token = None
        st.success("Logged out successfully")
        st.rerun()

else:
    st.info("You are already logged out")