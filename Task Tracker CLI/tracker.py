# 1. Add task
# 2. Update
# 3. Delete
# 4. View Tasks

tasks = [
    {"task": "Learn Python", "done": False},
    {"task": "Build CLI", "done": True}
]

def show_menu():
    print("--- Menu ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete/Remove Task")
    print("5. Exit App")


def add_task():
    task = input("Type here: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added! ")

def view_task():
    if not tasks:
        print("--- No Tasks Yet! ---")
        return
    
    print("\n--- To-Do List ---")
    for index, task in enumerate(tasks, start = 1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['task']} [{status}]")

def update_task():
    if not tasks:
            print("--- No Tasks Yet! ---")
            return
    else:
        view_task()

        try:
            index = int(input("\n Enter Task number to UPDATE: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                print("Marked as Done!")

            else:
                print("Invalid Number!")
        except ValueError:
            print("Please Enter a Valid Number.") 

def remove_task():
    if not tasks:
            print("--- No Tasks Yet! ---")
            return
    else:
        view_task()

        try:
            index = int(input("\n Enter Task number to Delete/Remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("Deleted The Task!")

            else:
                print("Invalid Number!")
        except ValueError:
            print("Please Enter a Valid Number.")



while True:
    show_menu()
    choice = int(input("\nEnter your CHOICE: "))
    print("-" * 65)

    if choice == 1:
        add_task()
        print("-" * 65)
        
    elif choice == 2:
        view_task()
        print("-" * 65)

    elif choice == 3:
        update_task()
        print("-" * 65)
        
    elif choice == 4:
        remove_task()
        print("-" * 65)
        
    elif choice == 5:
        print("--- See you Soon ---")
        print("-" * 65)
        break

    else:
        print("--- Invalid Choice - Re-Consider again---")
        print("-" * 65)
        # show_menu()