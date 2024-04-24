tasks = []


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear Completed Tasks")
    print("5. Exit")


def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")


def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")


def clear_completed():
    global tasks
    tasks = [task for task in tasks if not task["completed"]]
    print("Completed tasks cleared!")


while True:
    display_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        clear_completed()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

