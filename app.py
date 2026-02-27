from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/todos", methods=["GET"])
def get_todos():
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

    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    
    task = data.get("task")
    status = data.get("status", False)  # Default to False if not provided
    
    cur.execute("INSERT INTO todos (task, status) VALUES (%s, %s)", (task, status))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Task added successfully"})

if __name__ == "__main__":
    app.run(debug=True)