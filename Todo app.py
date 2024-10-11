
tasks = []


def add_task():
    task = input("Enter the task description: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for idx, task_info in enumerate(tasks, 1):
            status = "Completed" if task_info["completed"] else "Pending"
            print(f"{idx}. {task_info['task']} - {status}")


def mark_task_complete():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def show_menu():
    while True:
        print("\nTodo App Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

show_menu()
