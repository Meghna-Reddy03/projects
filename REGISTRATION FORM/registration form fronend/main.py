import streamlit as st
import requests

st.title("Registration Form")
cols = st.columns([0.5,4,0.5])
with cols[1]:
    full_name = st.text_input("Full Name")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.number_input('Age',placeholder='enter your age', min_value=0, max_value=120, step=1)
    location = st.text_input("Location")
    is_checked = st.checkbox('Accept terms and conditions')
    is_clicked = st.button('Submit',type='primary',use_container_width=True)
    if all((full_name,first_name,last_name,age,location,is_checked)):
        if is_clicked:
            backend_url = f"http://127.0.0.1:8000/create?full_name={full_name}&first_name={first_name}&last_name={last_name}&age={int(age)}&location={location}"
            res = requests.post(backend_url)
            if res.status_code == 200:
                st.toast("Registered Successfully!")
                res = res.json()
            else:
                st.toast('failed to register')
    else:
            st.toast('please fill the form')