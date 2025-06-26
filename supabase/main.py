from supabase import create_client
from fastapi import FastAPI

app = FastAPI()

supabase_url = "https://eiselzqyfstbfttivvfh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVpc2VsenF5ZnN0YmZ0dGl2dmZoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE4MDUsImV4cCI6MjA2NTM5NzgwNX0.6p75-Ye3zfMI4MilZrP6d2hat7G1PBtEArHHb9Uwupo"

database = create_client(supabase_url,supabase_key)

result = database.table("users").select('*').execute()

print(result.data)

@app.post("\login")
def login(username, password):
    result = database.table("app_users").select("*").eq('username', username).eq('password', password).execute()
    if len(result.data) > 0:
        return True
    else:
        return False

@app.get("/users")
def read_users():
    result_1  = database.table("users").select('*').execute()
    return result_1.data

@app.get("/create")
def create_user(name, age, password):
    result_2 = database.table("users").insert({
        'name':name,
        'age':age,
        'password': password
    }).execute()

    return result_2.data