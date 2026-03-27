class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def display(self):
        print(f"Title: {self.title} | Description: {self.description}")


task_list = []

def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    task_list.append(task)
    print(" Task Created Successfully!")

def read_tasks():
    if not task_list:
        print("No tasks available.")
    else:
        print("\n Task List:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. ", end="")
            task.display()

def update_task():
    read_tasks()
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(task_list):
        title = input("Enter new title: ")
        description = input("Enter new description: ")
        task_list[index].title = title
        task_list[index].description = description
        print("Task Updated!")
    else:
        print("Invalid task number!")

def delete_task():
    read_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(task_list):
        task_list.pop(index)
        print(" Task Deleted!")
    else:
        print("Invalid task number!")

# Menu System
while True:
    print("\n--- TASK MANAGER MENU ---")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        create_task()
    elif choice == '2':
        read_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice!")