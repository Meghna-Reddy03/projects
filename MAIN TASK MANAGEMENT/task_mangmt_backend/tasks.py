from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4
from datetime import datetime,timezone

tasks_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)

@tasks_router.get("/gettasks")
def get_tasks():
    result = db.table('task_management_tasks').select('*').execute()
    return result.data

@tasks_router.post("/tasks")
def create_task(project_id:str,description:str,title:str,assignee:str,priority:str,status:str,due_date:str,estimated_hours:float,actual_hours:float,team_member_id: str = ""):
    new_task = {
        'id':str(uuid4()),
        'description':description,
        'title':title,
        'assignee':assignee,
        'priority':priority,
        'status':status,
        'due_date':due_date,
        'project_id':project_id,
        'estimated_hours':estimated_hours,
        'actual_hours':actual_hours,
        'team_member_id':team_member_id,
        'created_at':datetime.now(timezone.utc).isoformat()
    }
    result = db.table('task_management_tasks').insert(new_task).execute()
    return {'project_id':project_id,'data':result.data}

@tasks_router.put("/updatetasks/{task_id}")
def update_task(
    task_id:str,
    title: str = "",
    description: str = "",
    assignee: str = "",
    priority: str = "",
    status: str = "",
    due_date: str = "",
    project_id:str="",
    team_member_id: str="",
    estimated_hours:float=0.0,
    actual_hours:float=0.0
    ):
    
    existing_info = db.table('task_management_tasks').select('*').eq('id',task_id).execute()

    if existing_info.data:
        update_info = {}
        if title != "":
            update_info["title"] = title
        if description != "":
            update_info["description"] = description
        if assignee != "":
            update_info['assignee']=assignee
        if priority != "":
            update_info["priority"] = priority
        if due_date != "":
            update_info["due_date"] = due_date
        if status != "":
            update_info["status"] = status
        if estimated_hours != 0.0:
            update_info["estimated_hours"] = estimated_hours
        if actual_hours != 0.0:
            update_info["actual_hours"] = actual_hours
        if project_id != "":
            update_info['project_id'] = project_id
        if team_member_id != "":
            update_info["team_member_id"] = team_member_id
        
        if update_info:
            updated_task = db.table('task_management_tasks').update(update_info).eq('id',task_id).execute()

            return {
                'message':'task updated successfuly',
                'updated_data':update_info,
                'updated_task':updated_task
            }
        else:
            return "nothing provided to update"
    else:
        return "Task not found"

@tasks_router.put("/taskstatus/{task_id}")
def update_task_status(task_id:str,status: str = ""):
    existing_status = db.table('task_management_tasks').select('status').eq('id',task_id).execute()
    
    if existing_status.data:
        update_status = {}
        if status != "":
            update_status["status"] = status
        if update_status:
            updated_status = db.table('task_management_tasks').update(update_status).eq('id',task_id).execute()
            return {
                'message':'task updated successfuly',
                'updated_status':updated_status
            }
        else:
            return "nothing provided to update"


   
@tasks_router.delete("/deltasks/{task_id}")
def delete_task(task_id: str):
    result = db.table("task_management_tasks").delete().eq("id", task_id).execute()
    return {
        "message": "🗑️ Task deleted successfully!",
        "project_id": task_id,
        "response": result.data
    }
    