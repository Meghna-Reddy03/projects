import streamlit as st
from supabase import create_client
import time

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)

single_file_url = ""

def upload_files(selected_files):
    multiple_file_urls = []
    for selected_image in selected_files:
        file_name = f"{selected_image.name}_{time.time()}"
        db.storage.from_('images').upload(file_name,selected_image.getvalue())
        single_file_url = db.storage.from_('images').get_public_url(file_name)
        multiple_file_urls.append(single_file_url)
    return multiple_file_urls



cols = st.columns([0.1,3,0.1])
with cols[1]:
    layout = st.columns([2,2,1])
    with layout[0]:
        st.text_input('username',placeholder='enter username',label_visibility='collapsed')
    with layout[1]:
        st.text_input('password',placeholder='enter password',type='password',label_visibility='collapsed')
    with layout[2]:
        st.button('Sign in',type='primary',use_container_width=True)
    st.divider()
    layout_2 = st.columns([3,1])
    with layout_2[0]:
        selected_files = st.file_uploader('upload your file',label_visibility='collapsed',accept_multiple_files = True,type=['jpg','png','jpeg'])
    with layout_2[1]:
        is_button_clicked = st.button('Upload')
    if is_button_clicked and selected_files:
        multiple_file_urls = upload_files(selected_files)
        for image in multiple_file_urls:
            st.image(image)