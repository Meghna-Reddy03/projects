from fastapi import APIRouter
from supabase import create_client
from uuid import uuid4

teams_router = APIRouter()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)

@teams_router.post('/teams')
def create_team(team_name:str,project_id:str):
    new_team ={
        'id':str(uuid4()),
        'team_name':team_name,
        'project_id':project_id
    }
    result=db.table('task_management_teams').insert(new_team).execute()
    return {
        "message": "Team created.",
        "team": result.data
    }

@teams_router.put('/teams/update/{team_id}')
def update_team(team_id:str,team_name:str="",project_id:str=""):
    existing_info=db.table('task_management_teams').select('*').eq('id',team_id).execute()
    if existing_info.data:
        update_info = {}
        if team_name != "":
            update_info['team_name']=team_name
        if project_id != "":
            update_info['project_id']=project_id

        if update_info:
            updated_team = db.table('task_management_teams').update(update_info).eq('id',team_id).execute()

            return {
                'message':'team updated successfuly',
                'updated_data':update_info,
                'updated_team':updated_team
            }
        else:
            return "nothing provided to update"
    else:
        return "Team not found"

@teams_router.delete("/delteams/{team_id}")
def delete_team(team_id: str):
    result_1 = db.table("task_management_teams").delete().eq("id", team_id).execute()
    return {
        "message": "Team deleted successfully!",
        "project_id": team_id,
        "response": result_1.data
    }
@teams_router.get("/getteams")
def get_teams():
    result_2 = db.table('task_management_teams').select('*').execute()
    return result_2.data