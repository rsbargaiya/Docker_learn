from db import get_connection

class Todo:

    def create_table(self):
        conn = get_connection()
        cur = conn.cursor()

        # Drop existing table if it exists
        cur.execute("DROP TABLE IF EXISTS todos CASCADE")

        # Create fresh table with timestamp
        cur.execute("""
        CREATE TABLE todos(
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL,
            status BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        cur.close()
        conn.close()

    def add_task(self, task):
        conn = get_connection()

        cur = conn.cursor()

        cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
        conn.commit()

        cur.close()
        conn.close()
        print("Task Added Successfully!")

    def view_tasks(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM todos ORDER BY id")
        rows = cur.fetchall()

        for row in rows:
            status = "✅ Done" if row[2] else "❌ Pending"
            created_at = row[3] if len(row) > 3 else "N/A"
            print(f"{row[0]} - {row[1]} - {status} - Created: {created_at}")

        cur.close()
        conn.close()

    def delete_task(self, task_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM todos WHERE id=%s", (task_id,))
        conn.commit()

        cur.close()
        conn.close()
        print("Task Deleted Successfully!")

    def mark_done(self, task_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("UPDATE todos SET status=TRUE WHERE id=%s", (task_id,))
        conn.commit()

        cur.close()
        conn.close()
        print("Task Marked as Done!")