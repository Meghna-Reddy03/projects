import streamlit as st

import requests

st.set_page_config(
    page_title='task manager',
    page_icon= "🗂️"
)

st.title('TASK MANAGER')
theme = st.selectbox("Theme",['light','dark'])
if theme == 'dark':
    st.markdown(
        """
        <style>
            body {
                background-color: #0E1117;
                color: #FAFAFA;
            }
            .stApp {
                background-color: #0E1117;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #F5F5DC;
                color: #000000;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
st.html("<p>hiiiiiiii</p>")