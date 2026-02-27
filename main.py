from app.db import create_table
from app.models import Todo

def main():
    print("\n--- TO DO APP ---")
    print("Creating table...")
    create_table()
    print("Table created!")
    
    while True:
        print("\n--- TO DO APP ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark as Done")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            Todo.add_task(task)
            print("✅ Task Added Successfully!")

        elif choice == "2":
            todos = Todo.get_all_tasks()
            if todos:
                for todo in todos:
                    status = "✅ Done" if todo['status'] else "❌ Pending"
                    print(f"{todo['id']} - {todo['task']} - {status} - Created: {todo['created_at']}")
            else:
                print("No tasks yet!")

        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            Todo.delete_task(int(task_id))
            print("✅ Task Deleted Successfully!")

        elif choice == "4":
            task_id = input("Enter task ID to mark done: ")
            Todo.mark_done(int(task_id))
            print("✅ Task Marked as Done!")

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()