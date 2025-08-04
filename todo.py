# file_name="todo.txt"
def add():
    task=input("Enter task:")
    with open(file_name,"a") as f:
        f.write(task+"\n")
    print("Task Added successfully")
def view():
    try:
        with open(file_name,"r") as f:
            task=f.readlines()
            if not task:
                print("No tasks found")
            else:
                 for index,task in enumerate(task,start=1):
                        print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print('Not tasks to do')
def remove():
    try:
            with open (file_name,"r")as f:
                task=f.readlines()
                if not task:
                    print("No task to remove")
                    return
            view()
            task_num=int(input("Enter the task number to remove"))
            if 1<=task_num <=len(task):
                remove=task.pop(task_num-1)
                with open(file_name,"w")as f:
                    f.writelines(task)
                print("Task removed")
            else:
                 print("Invalid task number")
    except FileNotFoundError:
        print("No task found")
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        remove()
    elif choice == "4":
        print("Exit!")
        break
    else:
        print("Invalid choice. Please try again.")  
    
