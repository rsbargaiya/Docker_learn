from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoCreate(BaseModel):
    task: str
    status: bool = False

class TodoResponse(BaseModel):
    id: int
    task: str
    status: bool
    created_at: Optional[str] = None

    class Config:
        from_attributes = True
