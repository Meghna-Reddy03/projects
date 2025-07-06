from fastapi import FastAPI
from projects import projects_router
from tasks import tasks_router
from teams import teams_router
from team_members import team_member_router

app = FastAPI()

app.include_router(projects_router)
app.include_router(tasks_router)
app.include_router(teams_router)
app.include_router(team_member_router)