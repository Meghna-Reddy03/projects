from fastapi import FastAPI
from supabase import create_client


app = FastAPI(
    title="registration form",
    description='simple registration form'
)

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

db = create_client(supabase_url,supabase_key)


@app.post("/create")
def create_form(full_name:str,first_name:str,last_name:str,age:int,location:str):
    result = db.table('user_details').insert({
        'full_name':full_name,
        'first_name':first_name,
        'last_name':last_name,
        'age':age,
        'location':location
    }).execute()
    return result.data

@app.get("/check")
def check():
    result_1 = db.table('user_details').select('*').execute()
    return result_1.data

