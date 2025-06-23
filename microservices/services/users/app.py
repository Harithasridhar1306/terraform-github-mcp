from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Users service is running!"}


class User(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    return {"message": f"User {user.name} added!", "data": user}
