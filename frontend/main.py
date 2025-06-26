import streamlit as st
from api import login

cols = st.columns([1, 3, 1])

with cols[1]:
    st.header("Login / Register")
    username = st.text_input("Username", placeholder="Enter username")
    password = st.text_input("Password", placeholder="Enter password", type="password")
    is_checked = st.checkbox("Accept Terms and Conditions")
    is_clicked = st.button("Login", type="primary", use_container_width=True)
    if is_clicked:
        if username and password and is_checked:
            data = login(username, password)
            if data:
                st.toast("Login successful")
            else:
                st.toast('invalid credentials')
        else:
            st.toast("Please fill the form")