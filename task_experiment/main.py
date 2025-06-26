from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.post("/task/add")
def add_task(title, desc):
    tasks.append({"title": title, "description": desc})
    return {"message": "Task added", "tasks": tasks}

@app.get("/task/get")
def get_tasks():
    return {"tasks": tasks}


@app.put("/task/update")
def update_task(title,new_desc):
    for task in tasks:
        if task["title"] == title:
            task["description"] = new_desc
            return tasks
    return "Task not found"


@app.delete("/task/delete")
def delete_task(title):
    for i in tasks:
        if tasks["title"] == title:
            tasks.pop(i)
            return tasks
    return "Task not found"
