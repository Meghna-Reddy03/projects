import streamlit as st
from supabase import create_client
from datetime import datetime
import uuid


supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"
db = create_client(supabase_url,supabase_key)

st.header("Time Tracking")

with st.form("time_tracking_form"):
    task_id = st.text_input("Task ID")
    user_name = st.text_input("Your Name")
    
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
        start_time = st.time_input("Start Time")
    with col2:
        end_date = st.date_input("End Date")
        end_time = st.time_input("End Time")

    description = st.text_area("Task Description")
    billable = st.checkbox("Is this billable?", value=True)
    hourly_rate = st.number_input("Hourly Rate (₹)", min_value=0.0, format="%.2f")

    submit = st.form_submit_button("Log Time",type='primary',use_container_width=True)

if submit:
    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    duration = int((end_datetime - start_datetime).total_seconds() / 60)

    start_time_format = start_datetime.isoformat()
    end_time_format = end_datetime.isoformat()

    payload = {
        "task_id": task_id,
        "user_name": user_name,
        "start_time": start_time_format,
        "end_time": end_time_format,
        "duration_minutes": duration,
        "description": description,
        "billable": billable,
        "hourly_rate": hourly_rate,
    }
    st.subheader("Time Log Preview")
    st.json(payload)

    response = db.table("task_management_time_tracking").insert(payload).execute()

    if response.data:
        st.json(response.data)
    
    else:
         st.error("Something went.")
