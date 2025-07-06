from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4

team_member_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)

@team_member_router.post("/teammember")
def create_team_member(user_name: str,mail_id:str,role:str,hourly_pay:float,team_id:str):
    new_team_member = {
        "id": str(uuid4()),
        "user_name": user_name,
        "mail_id":mail_id,
        "team_id":team_id,
        "role":role,
        'hourly_pay':hourly_pay

    }
    result = db.table("task_management_team_members").insert(new_team_member).execute()
    return {
        "message": "Team member created.",
        "team": result.data
    }

@team_member_router.put("/teammember/update/{team_id}")
def add_team_member(team_id:str,user_name: str='',mail_id:str='',role:str='',hourly_pay:float=0.0):
    existing_info = db.table('task_management_team_members').select('*').eq('id',team_id).execute()
    if existing_info.data:
        updated_info={}
        if user_name != "":
            updated_info['user_name']=user_name
        if mail_id != "":
            updated_info['mail_id']=mail_id
        if role != "":
            updated_info['role']=role
        if hourly_pay != 0.0:
            updated_info['hourly_pay']=hourly_pay
        
        if updated_info:
            updated_team_member=db.table('task_management_team_members').update(updated_info).eq('id',team_id).execute()
            return {
                'message':'team member updated successfuly',
                'updated_data':updated_info,
                'updated_team_member':updated_team_member
            }
        else:
            return "nothing provided to update"
    else:
        return "Team member not found"
        
@team_member_router.delete("/teammember/delete/{team_id}")
def delete_team_member(team_id:str):
    result_1=db.table('task_management_team_members').delete().eq('id',team_id).execute()
    return {
        "message": "Team member deleted successfully!",
        "team_id": team_id,
        "response": result_1.data
    }
@team_member_router.get("/getteammembers")
def get_team_member():
    result_2 = db.table('task_management_team_members').select('*').execute()
    return result_2.data