import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['task']} [{status}]")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
        tasks[choice - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid choice.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Task '{removed['task']}' deleted!")
    except (IndexError, ValueError):
        print("Invalid choice.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
