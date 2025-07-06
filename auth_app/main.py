from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def home():
    return 'hello world, learning python'