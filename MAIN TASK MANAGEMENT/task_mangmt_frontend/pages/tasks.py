import streamlit as st
import requests
from datetime import date

st.header('Tasks')
tab_create, tab_update, tab_status, tab_delete, tab_get = st.tabs(['CREATE TASK', 'UPDATE TASK', 'UPDATE STATUS', 'DELETE TASK', 'GET TASKS'])

# CREATE TASK
with tab_create:
    st.markdown('Create a new task')
    cols = st.columns([1, 3, 1])
    with cols[1]:
        with st.form('create_task_form'):
            title = st.text_input("Task Title")
            description = st.text_area("Task Description")
            assignee = st.text_input("Assignee")
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
            status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
            due_date = st.date_input("Due Date", value=date.today())
            estimated_hours = st.number_input("Estimated Hours", min_value=0.0, format="%.2f")
            actual_hours = st.number_input("Actual Hours", min_value=0.0, format="%.2f")
            project_id = st.text_input("Project ID")
            team_member_id = st.text_input("Team Member ID (optional)", placeholder="Leave blank if not assigned")

            create_btn = st.form_submit_button("Create Task", type='primary', use_container_width=True)

        if create_btn:
            payload = {
                "title": title,
                "description": description,
                "assignee": assignee,
                "priority": priority,
                "status": status,
                "due_date": str(due_date),
                "estimated_hours": estimated_hours,
                "actual_hours": actual_hours,
                "project_id": project_id,
                "team_member_id": team_member_id
            }

            response = requests.post("http://127.0.0.1:8000/tasks", params=payload)

            if response.status_code == 200:
                st.success("Task created successfully!")
            else:
                st.error("Failed to create task.")

# PUT - Update Task
with tab_update:
    st.markdown("Update a task")
    with st.form("update_task_form"):
        task_id = st.text_input("Task ID")
        title = st.text_input("New Title", placeholder="(optional)")
        description = st.text_area("New Description", placeholder="(optional)")
        assignee = st.text_input("New Assignee", placeholder="(optional)")
        priority = st.selectbox("New Priority", ["", "Low", "Medium", "High"])
        status = st.selectbox("New Status", ["", "Not Started", "In Progress", "Completed"])
        due_date = st.text_input("New Due Date (YYYY-MM-DD)", placeholder="(optional)")
        estimated_hours = st.number_input("Estimated Hours", value=0.0, format="%.2f")
        actual_hours = st.number_input("Actual Hours", value=0.0, format="%.2f")
        project_id = st.text_input("New Project ID", placeholder="(optional)")
        team_member_id = st.text_input("New Team Member ID", placeholder="(optional)")

        update_btn = st.form_submit_button("Update Task")

    if update_btn:
        payload = {
            "title": title,
            "description": description,
            "assignee": assignee,
            "priority": priority,
            "status": status,
            "due_date": due_date,
            "estimated_hours": estimated_hours,
            "actual_hours": actual_hours,
            "project_id": project_id,
            "team_member_id": team_member_id
        }

        response = requests.put(f"http://127.0.0.1:8000/updatetasks/{task_id}", params=payload)

        if response.status_code == 200:
            st.success("Task updated successfully!")
            st.json(response.json())
        else:
            st.error("Failed to update task.")

# PUT - Update Task Status 
with tab_status:
    st.markdown("Update task status only")
    with st.form("update_status_form"):
        task_id = st.text_input("Task ID")
        status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"])
        status_btn = st.form_submit_button("Update Status")

    if status_btn:
        response = requests.put(f"http://127.0.0.1:8000/taskstatus/{task_id}", params={"status": status})
        if response.status_code == 200:
            st.success("Status updated successfully!")
            st.json(response.json())
        else:
            st.error("Failed to update status.")

# DELETE - Delete Task
with tab_delete:
    st.markdown("Delete a task")
    del_id = st.text_input("Enter Task ID to delete")

    if st.button("Delete Task"):
        response = requests.delete(f"http://127.0.0.1:8000/deltasks/{task_id}")
        if response.status_code == 200:
            st.success(f"Task {del_id} deleted successfully!")
        else:
            st.error("Failed to delete. Task may not exist.")

# GET - Get All Tasks
with tab_get:
    st.markdown("All Tasks")
    if st.button("Refresh Task List"):
        res = requests.get("http://127.0.0.1:8000/gettasks")
        if res.status_code == 200:
            data = res.json()
            if data:
                for task in data:
                    with st.expander(task["title"]):
                        st.write(f"ID: {task['id']}")
                        st.write(f"Description: {task['description']}")
                        st.write(f"Assignee: {task['assignee']}")
                        st.write(f"Priority: {task['priority']}")
                        st.write(f"Due Date: {task['due_date']}")
                        st.write(f"Estimated: {task['estimated_hours']} hrs | Actual: {task['actual_hours']} hrs")
                        st.write(f"Project ID: {task['project_id']}")
                        st.write(f"Team Member ID: {task['team_member_id']}")
                        st.write(f"Status: {task['status']}")
            else:
                st.info("No tasks found.")
        else:
            st.error("Failed to load tasks.")
