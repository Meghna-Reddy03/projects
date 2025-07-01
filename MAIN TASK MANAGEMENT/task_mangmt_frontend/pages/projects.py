import streamlit as st
from datetime import date
import requests

st.header('Projects')
tab_create, tab_update, tab_delete, tab_get = st.tabs(['CREATE PROJECT','UPDATE PROJECT','DELETE PROJECT','GET PROJECT'])
cols = st.columns([1,3,1])

#POST
with tab_create:
    st.markdown('Create a project')
    cols = st.columns([1, 3, 1]) 
    with cols[1]:
        with st.form('Create a new project'):
            name = st.text_input('Project name')
            description = st.text_area("Description")
            
            cols_1 = st.columns([1, 0.5, 1])
            with cols_1[0]:
                start_date = st.date_input("Start Date", value=date.today())
            with cols_1[2]:
                end_date = st.date_input("End Date", value=date.today())
            with cols_1[0]:
                status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
            with cols_1[2]:
                budget = st.number_input("Budget", min_value=0.0, format="%.2f")
            
            cols_2 = st.columns([1, 2, 1])
            with cols_2[1]:
                submit_form = st.form_submit_button('Create Project', type='primary', use_container_width=True)

                if submit_form:
                    payload = {
                        "name": name,
                        "description": description,
                        "start_date": str(start_date),
                        "end_date": str(end_date),
                        "status": status,
                        "budget": budget
                    }

                    response = requests.post('http://127.0.0.1:8000/projects', params=payload)

                    if response.status_code == 200:
                        st.success("Project created successfully!")
                    else:
                        st.error("Failed to create project.")

#UPDATE
with tab_update:
    st.markdown("Update a project")

    with st.form("update_project_form"):
        project_id = st.text_input("Enter Project ID to update")
        name = st.text_input("New name",placeholder="(optional)")
        description = st.text_area("New description",placeholder="(optional)")
        start_date = st.text_input("Start Date (YYYY-MM-DD)", placeholder="(optional)")
        end_date = st.text_input("End Date (YYYY-MM-DD)", placeholder="(optional)")
        status = st.selectbox("Status", ["", "Not Started", "In Progress", "Completed"])
        budget = st.number_input("New Budget (₹)", value=0.0, format="%.2f")

        update_btn = st.form_submit_button("Update Project")

    if update_btn:
        payload = {
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "budget": budget
        }

        update_url = f"http://127.0.0.1:8000/updateprojects/{project_id}"
        response = requests.put(update_url, params=payload)

        if response.status_code == 200:
            st.success("Project updated successfully!")
            st.json(response.json())
        else:
            st.error("Failed to update project.")

#DELETE 
with tab_delete:
    st.markdown("Delete a project")
    del_id = st.text_input("Enter Project ID to delete")

    if st.button("Delete Project"):
        del_url = f"http://127.0.0.1:8000//delprojects/{project_id}"
        response = requests.delete(del_url)

        if response.status_code == 200:
            st.success(f"Project {del_id} deleted successfully!")
        else:
            st.error("Failed to delete. Project may not exist.")

#GET
with tab_get:
    st.markdown("All Projects")
    if st.button("Refresh List"):
        res = requests.get("http://127.0.0.1:8000/check")
        if res.status_code == 200:
            data = res.json()
            if data:
                for p in data:
                    with st.expander(p["name"]):
                        st.write(f"ID: {p['id']}")
                        st.write(f"Description: {p['description']}")
                        st.write(f"Start: {p['start_date']} → End: {p['end_date']}")
                        st.write(f"Status: {p['status']}")
                        st.write(f"Budget: ₹{p['budget']}")
            else:
                st.info("No projects found!")
        else:
            st.error("Failed to load projects.")
