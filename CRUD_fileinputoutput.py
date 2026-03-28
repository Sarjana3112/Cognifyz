import os

FILE_NAME = "tasks.txt"

class Task:
    def __init__(self, title):
        self.title = title

def load_tasks():
    tasks = []
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                for line in file:
                    tasks.append(Task(line.strip()))
    except Exception as e:
        print("Error loading file:", e)
    return tasks

def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(task.title + "\n")
    except Exception as e:
        print("Error saving file:", e)

tasks = load_tasks()

def add_task():
    title = input("Enter task title: ")
    tasks.append(Task(title))
    save_tasks(tasks)
    print("Task saved to file!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.title}")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

while True:
    print("\n--- FILE TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")