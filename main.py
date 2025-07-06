import streamlit as st
 

cols = st.columns([1,3,1])
st.set_page_config(page_title="Task Manager", layout="wide")
with cols[1]:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.header('Welcome to task manager app!')
    st.markdown("""
    
    ✅ Track time  
    📁 Manage projects  
    👥 Collaborate with your team  
    📊 Analyze productivity  
    """)
    st.info("Use the sidebar to navigate through the app!")



