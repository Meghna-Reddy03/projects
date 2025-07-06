from fastapi import FastAPI
from controller import router
app = FastAPI(
    title="URL Shortner",
    description="A simple backend to create shorten URLs for user accessibility"
)

app.include_router(router)