# Database Models/Operations

class Todo:
    
    @staticmethod
    def add_task(task, status=False):
        from .db import get_connection
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO todos (task, status) VALUES (%s, %s)", (task, status))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Task Added Successfully!"}
    
    @staticmethod
    def get_all_tasks():
        from .db import get_connection
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM todos ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        todos = []
        for row in rows:
            todos.append({
                "id": row[0],
                "task": row[1],
                "status": row[2],
                "created_at": str(row[3]) if len(row) > 3 else None
            })
        return todos
    
    @staticmethod
    def delete_task(task_id):
        from .db import get_connection
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM todos WHERE id=%s", (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Task Deleted Successfully!"}
    
    @staticmethod
    def mark_done(task_id):
        from .db import get_connection
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE todos SET status=TRUE WHERE id=%s", (task_id,))
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Task Marked as Done!"}
