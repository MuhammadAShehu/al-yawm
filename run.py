tasks = []
def add_task(task):
    tasks.append(task)

def list_tasks():
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks")

def delete_task(index):
    try:
        del tasks[index]
        print("Task deleted successfully")
    except IndexError:
        print("Invalid task index")

def main():
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    