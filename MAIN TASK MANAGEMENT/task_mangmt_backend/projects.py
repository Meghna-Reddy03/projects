from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4
from datetime import datetime,timezone

projects_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)
#PROJECTS

@projects_router.get("/check")
def get_projects():
    result_1 = db.table('task_management_projects').select('*').execute()
    return result_1.data


@projects_router.post("/projects")
def create_project(name:str,description:str,start_date:str,end_date:str,status:str,budget:float):
    new_project = {
        'id':str(uuid4()),
        'name':name,
        'description':description,
        'start_date':start_date,
        'end_date':end_date,
        'status':status,
        'budget':budget,
        'created_at':datetime.now(timezone.utc).isoformat()
    }
    result = db.table('task_management_projects').insert(new_project).execute()
    return result.data


@projects_router.put("/updateprojects/{project_id}")
def update_project(
    project_id:str,
    name: str = "",
    description: str = "",
    start_date: str = "",
    end_date: str = "",
    status: str = "",
    budget: float = 0.0
    ):
    
    existing_info = db.table('task_management_projects').select('*').eq('id',project_id).execute()

    if existing_info.data:
        update_info = {}
        if name != "":
            update_info["name"] = name
        if description != "":
            update_info["description"] = description
        if start_date != "":
            update_info["start_date"] = start_date
        if end_date != "":
            update_info["end_date"] = end_date
        if status != "":
            update_info["status"] = status
        if budget != 0.0:
            update_info["budget"] = budget
        
        if update_info:
            updated_project = db.table('task_management_projects').update(update_info).eq('id',project_id).execute()

            return {
                'message':'project updated successfuly',
                'updated_data':update_info,
                'updated_project':updated_project
            }
        else:
            return "nothing provided to update"
    else:
        return "Project not found"
    
@projects_router.delete("/delprojects/{project_id}")
def delete_project(project_id: str):
    result = db.table("task_management_projects").delete().eq("id", project_id).execute()
    return {
        "message": "🗑️ Project deleted successfully!",
        "project_id": project_id,
        "response": result.data
    }