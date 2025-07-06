import streamlit as st
import requests

st.header("Team Members")
tab_create, tab_update, tab_delete, tab_get = st.tabs(["CREATE MEMBER", "UPDATE MEMBER", "DELETE MEMBER", "GET MEMBERS"])

API_URL = "http://127.0.0.1:8000"

# CREATE TEAM MEMBER
with tab_create:
    st.markdown("Add a new team member to your squad ")
    with st.form("create_team_member_form"):
        user_name = st.text_input("Name")
        mail_id = st.text_input("Email")
        role = st.text_input("Role")
        hourly_pay = st.number_input("Hourly Pay (₹)", min_value=0.0, format="%.2f")
        team_id = st.text_input("Team ID")
        create_btn = st.form_submit_button("Create Member", type='primary', use_container_width=True)

    if create_btn:
        payload = {
            "user_name": user_name,
            "mail_id": mail_id,
            "role": role,
            "hourly_pay": hourly_pay,
            "team_id": team_id
        }

        response = requests.post(f"{API_URL}/teammember", params=payload)

        if response.status_code == 200:
            st.success("Team member added successfully! ")
            st.json(response.json())
        else:
            st.error("Something went wrong. Couldn't add the team member.")

# UPDATE TEAM MEMBER
with tab_update:
    st.markdown("Update team member info ")
    with st.form("update_team_member_form"):
        member_id = st.text_input("Team Member ID")
        user_name = st.text_input("New Name", placeholder="(optional)")
        mail_id = st.text_input("New Email", placeholder="(optional)")
        role = st.text_input("New Role", placeholder="(optional)")
        hourly_pay = st.number_input("New Hourly Pay", min_value=0.0, format="%.2f")

        update_btn = st.form_submit_button("Update Member")

    if update_btn:
        payload = {
            "user_name": user_name,
            "mail_id": mail_id,
            "role": role,
            "hourly_pay": hourly_pay
        }

        response = requests.put(f"{API_URL}/teammember/update/{member_id}", params=payload)

        if response.status_code == 200:
            st.success("Member updated successfully ")
            st.json(response.json())
        else:
            st.error("Update failed.Check if ID is correct.")

# DELETE TEAM MEMBER
with tab_delete:
    st.markdown("Delete a team member ")
    del_id = st.text_input("Enter Team Member ID")

    if st.button("Delete Member"):
        response = requests.delete(f"{API_URL}/teammember/delete/{del_id}")

        if response.status_code == 200:
            st.success(f"Team member {del_id} deleted!")
            st.json(response.json())
        else:
            st.error("Failed to delete member. Check if the ID exists.")

# GET TEAM MEMBERS
with tab_get:
    st.markdown("All Team Members")

    if st.button("Refresh Member List"):
        res = requests.get(f"{API_URL}/getteammembers")
        if res.status_code == 200:
            members = res.json()
            if members:
                for member in members:
                    with st.expander(f"{member['user_name']} ({member['role']})"):
                        st.write(f"ID: {member['id']}")
                        st.write(f"Email: {member['mail_id']}")
                        st.write(f"Team ID: {member['team_id']}")
                        st.write(f"Hourly Pay: ₹{member['hourly_pay']}")
            else:
                st.info("No members found.")
        else:
            st.error("Error fetching members.")

