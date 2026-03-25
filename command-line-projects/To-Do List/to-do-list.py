# Tyree Franklin Jr.
# To-Do List Project
# Description:
# This is a simple command-line app where the user can:
#   add tasks, view tasks, mark tasks complete, and delete tasks
# 
# It includes beginner skills such as:
#   variables, lists, functions, loops, conditionals,
#   user input, dictionaries, f-strings, and string formatting

import os

# Declare Essential Functions
def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system("clear")

def section():
    print("==============================================")

def choice_validation(choice):
    while choice < 0 or choice > 4:
        print("Incorrect input, please enter choices 1-4. Input '0' to quit.")
        choice = int(input("Follow the instructions below to get started:\n(0) Quit App\n(1) Add Tasks\n(2) View Tasks\n(3) Mark Task Complete\n(4) Delete tasks\n\nInput: "))

# To-Do List Menu
clear_screen()
section()
print("Tyree's To-Do List Manager\n")
section()
choice = int(input("Follow the instructions below to get started:\n(0) Quit App\n(1) Add Tasks\n(2) View Tasks\n(3) Mark Task Complete\n(4) Delete tasks\n\nInput: "))
section()

# Validate the user's input
choice_validation(choice)
tasks = []
user_tasks = {}

running = True

# Add a Task
def add_task():
    clear_screen()
    print("Add Task")
    print("Enter a task that you'd like to complete.")

    task = str(input("Task: "))
    user_tasks[task] = False
    tasks.append(task)

    print("\nSuccessfully saved the task!")

# View the task
def view_tasks():
    clear_screen()
    print("Your Tasks\n")
    list_item = 1

    for task in tasks:
        if task in user_tasks:

            if user_tasks[task] == True:
                status = "Complete"
            else:
                status = "Incomplete"

            print(f"{list_item}. {task} - {status}")

        else:
            print(f"Failed to find task status for '{task}'")
        list_item += 1

# Mark the task complete
def mark_complete():
    clear_screen()
    section()

    print("Mark Task Complete\n")
    print("Enter the task number that you'd like to mark as complete: ")

    list_item = 1
    count = 0
    length = 0

    for task in tasks:
        if task in user_tasks and user_tasks[task] == False:
            print(f"{list_item}. {task}")
            count += 1
            list_item += 1
            length += 1

    if length == 0:
        print("You have no incomplete tasks.")
        return

    else:
        selection = int(input("\nInput: "))

        # Find the selection and delete it
        if selection > 0 and selection <= count:
            count = 0

            for task in tasks:
                if task in user_tasks and user_tasks[task] == False:
                    if count + 1 == selection:
                        user_tasks[task] = True
                        break
                    count += 1

        clear_screen()

# Delete a task
def delete_task():
    clear_screen()
    section()
    print("Delete Task")
    print("Enter the task number that you'd like to delete from the list")

    list_item = 1

    for task in tasks:
        if task in user_tasks:

            if user_tasks[task] == True:
                status = "Complete"
            else:
                status = "Incomplete"

            print(f"{list_item}. {task} - {status}")

        else:
            print(f"Failed to find task status for '{task}'")
        list_item += 1

    selection = int(input("\nInput: "))

    if selection > 0 and selection < list_item:
        count = 0

        for task in tasks:
            if count + 1 == selection:
                del user_tasks[task]
                tasks.remove(task)
                print(f"Deleted task {task}")
                break
            count += 1

    clear_screen()

# Input management
while running:
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        mark_complete()
    elif choice == 4:
        delete_task()
    elif choice == 0:
        running = False
    
    # User input
    section()
    print("Tyree's To-Do List Manager\n")
    section()
    choice = int(input("Follow the instructions below to get started:\n(0) Quit App\n(1) Add Tasks\n(2) View Tasks\n(3) Mark Task Complete\n(4) Delete tasks\n\nInput: "))
    section()
