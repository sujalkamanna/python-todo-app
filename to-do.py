tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\nMenu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tasks.append(input("Enter task: "))
    elif choice == '2':
        if tasks:
            idx = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= idx < len(tasks):
                print(f"Task '{tasks.pop(idx)}' marked as completed.")
            else:
                print("Invalid task number")
        else:
            print("No tasks to mark as completed")
    elif choice == '3':
        if tasks:
            idx = int(input("Enter task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                print(f"Task '{tasks.pop(idx)}' removed.")
            else:
                print("Invalid task number")
        else:
            print("No tasks to remove")
    elif choice == '4':
        break
    else:
        print("Invalid input")
