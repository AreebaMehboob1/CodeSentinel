import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from JSON file (if exists)
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task}' added successfully!")

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑 Task '{removed}' removed successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks found.")
    else:
        print("\n📝 To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List App =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("📌 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
