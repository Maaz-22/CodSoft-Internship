# Task 1
todo_list = []


def display_todo_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def update_task():
    display_todo_list()
    task_number = int(input("Enter the number of the task to update: "))

    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
        return

    new_task = input("Enter the new task: ")
    todo_list[task_number - 1] = new_task
    print("Task updated.")

def delete_task():
    display_todo_list()
    task_number = int(input("Enter the number of the task to remove: "))

    if task_number < 1 or task_number > len(todo_list):
        print("Invalid task number.")
        return

    removed_task = todo_list.pop(task_number - 1)
    print(f"Task '{removed_task}' removed from the to-do list.")

while True:
    print("\nTo-Do List Application")
    print("1. Display to-do list")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please try again.")
