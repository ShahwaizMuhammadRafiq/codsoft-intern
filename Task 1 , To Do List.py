tasks = []
print("\t\t\t To Do List Application")
while True:
    print("\nTask List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task",task,"added to the task list.")
    elif choice == "2":
        if not tasks:
            print("No tasks in the list")
        else:
            print("Task List:")
            for index, task in enumerate(tasks, start=1):
                print(index,task)
    elif choice == "3":
        if not tasks:
            print("No tasks in the list.")
        else:
            taskindex = int(input("Enter the task index to mark as completed: "))
            if 1 <= taskindex <= len(tasks):
                completedtask = tasks.pop(taskindex - 1)
                print("Task", completedtask, "marked as completed.")
            else:
                print("Invalid task index.")
    elif choice == "4":
        print("Exiting the Task List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
