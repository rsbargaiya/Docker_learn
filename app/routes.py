from fastapi import APIRouter, HTTPException
from .models import Todo
from .schemas import TodoCreate, TodoResponse

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list)
def get_todos():
    """Get all todos"""
    todos = Todo.get_all_tasks()
    return todos

@router.post("/", response_model=dict, status_code=201)
def add_todo(todo: TodoCreate):
    """Add a new todo"""
    Todo.add_task(todo.task, todo.status)
    return {"message": "Task added successfully"}

@router.delete("/{task_id}", response_model=dict)
def delete_todo(task_id: int):
    """Delete a todo by ID"""
    result = Todo.delete_task(task_id)
    return result

@router.put("/{task_id}/done", response_model=dict)
def mark_todo_done(task_id: int):
    """Mark a todo as done"""
    result = Todo.mark_done(task_id)
    return result

