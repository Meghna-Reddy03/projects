import streamlit as st
import requests

st.header("Teams")
tab_create, tab_update, tab_delete, tab_get = st.tabs(["CREATE TEAM", "UPDATE TEAM", "DELETE TEAM", "GET TEAMS"])

BASE_URL = "http://127.0.0.1:8000"  

# CREATE TEAM
with tab_create:
    st.subheader("Create a New Team")
    with st.form("create_team_form"):
        team_name = st.text_input("Team Name")
        project_id = st.text_input("Project ID")
        create_btn = st.form_submit_button("Create Team", type="primary", use_container_width=True)

    if create_btn:
        payload = {"team_name": team_name, "project_id": project_id}
        try:
            response = requests.post(f"{BASE_URL}/teams", params=payload)
            if response.status_code == 200:
                st.success("Team created successfully!")
                st.json(response.json())
            else:
                st.error("Failed to create team.")
        except Exception as e:
            st.error(f"Error: {e}")

# UPDATE TEAM
with tab_update:
    st.subheader("Update Existing Team")
    with st.form("update_team_form"):
        team_id = st.text_input("Team ID")
        new_team_name = st.text_input("New Team Name", placeholder="Leave blank if not updating")
        new_project_id = st.text_input("New Project ID", placeholder="Leave blank if not updating")
        update_btn = st.form_submit_button("Update Team")

    if update_btn:
        payload = {
            "team_name": new_team_name,
            "project_id": new_project_id
        }
        try:
            response = requests.put(f"{BASE_URL}/teams/update/{team_id}", params=payload)
            if response.status_code == 200:
                st.success("Team updated successfully!")
                st.json(response.json())
            else:
                st.error("Failed to update team.")
        except Exception as e:
            st.error(f"Error: {e}")

# DELETE TEAM
with tab_delete:
    st.subheader("Delete a Team")
    team_id_to_delete = st.text_input("Team ID to Delete")
    if st.button("Delete Team"):
        try:
            response = requests.delete(f"{BASE_URL}/delteams/{team_id_to_delete}")
            if response.status_code == 200:
                st.success(f"Team {team_id_to_delete} deleted successfully!")
                st.json(response.json())
            else:
                st.error("Failed to delete team.")
        except Exception as e:
            st.error(f"Error: {e}")

# GET TEAMS
with tab_get:
    st.subheader("All Teams")
    if st.button("Load Teams"):
        try:
            response = requests.get(f"{BASE_URL}/getteams")
            if response.status_code == 200:
                teams = response.json()
                if teams:
                    for team in teams:
                        with st.expander(f"Team: {team['team_name']}"):
                            st.write(f"ID: {team['id']}")
                            st.write(f"Project ID: {team['project_id']}")
                else:
                    st.info("No teams found.")
            else:
                st.error("Failed to fetch teams.")
        except Exception as e:
            st.error(f"Error: {e}")
