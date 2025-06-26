import streamlit as st
import requests

cols = st.columns([1,3,1])

with cols[1]:
    st.title("URL SHORTNER")
    st.divider()
    long_url = st.text_input('Enter URL',placeholder='enter long url')
    is_clicked = st.button('enter',type='primary',use_container_width=True)
    if long_url and is_clicked:
        res = requests.post(f"http://127.0.0.1:8000/shorten?long_url={long_url}")
        if res.status_code == 200:
            st.toast('successfully url generated')
            res = res.json()
            st.write(res)
