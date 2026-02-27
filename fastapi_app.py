from fastapi import FastAPI
from pydantic import BaseModel
from db import get_connection

app = FastAPI()

class Todo(BaseModel):
    task: str
    status: bool = False  # Optional, defaults to False

@app.get("/todos")
def get_todos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [{"id": r[0], "task": r[1], "status": r[2], "created_at": str(r[3]) if len(r) > 3 else None} for r in rows]

@app.post("/todos")
def add_todo(todo: Todo):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (task, status) VALUES (%s, %s)", (todo.task, todo.status))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Task added"}
