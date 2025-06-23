from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Tasks service is running!"}

class Task(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks")
def create_task(task: Task):
    return {"message": f"Task '{task.title}' created.", "data": task}
