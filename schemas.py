from pydantic import BaseModel

class TodoCreate(BaseModel):
    task: str

class UserCreate(BaseModel):
    username: str
    password: str