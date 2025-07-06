import streamlit as st
import requests

st.header("Team Management")
tab_create_team, tab_add_member = st.tabs(["CREATE TEAM", "ADD MEMBER"])

# CREATE TEAM 
with tab_create_team:
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.subheader("Create a New Team")

        with st.form("create_team_form"):
            team_name = st.text_input("Team Name")
            team_email = st.text_input("Team Email")
            team_role = st.text_input("Role")
            hourly_rate = st.number_input("Hourly Rate (₹)", min_value=0.0, format="%.2f")

            team_submit = st.form_submit_button("Create Team", use_container_width=True,type='primary')

        if team_submit:
            params = {
                "name": team_name,
                "email": team_email,
                "role": team_role,
                "hourly_rate": hourly_rate
            }

            res = requests.post("http://127.0.0.1:8000/teams", params=params)

            if res.status_code == 200:
                st.success("Team created successfully!")
                st.json(res.json())
            else:
                st.error("Failed to create team.")

# ADD TEAM MEMBER 
with tab_add_member:
    cols = st.columns([1, 3, 1])
    with cols[1]:
        st.subheader("Add a Team Member")

        with st.form("add_member_form"):
            member_name = st.text_input("Member Name")
            member_email = st.text_input("Member Email")
            member_role = st.text_input("Role")
            member_hourly_rate = st.number_input("Hourly Rate (₹)", min_value=0.0, format="%.2f", key="member_rate")

            member_submit = st.form_submit_button("Add Member", use_container_width=True,type='primary')

        if member_submit:
            params = {
                "name": member_name,
                "email": member_email,
                "role": member_role,
                "hourly_rate": member_hourly_rate
            }

            dummy_team_id = "any-id"
            res = requests.post(f"http://127.0.0.1:8000/teams/{dummy_team_id}/members", params=params)

            if res.status_code == 200:
                st.success("Member added successfully!")
                st.json(res.json())
            else:
                st.error("Failed to add team member.")

