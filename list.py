#Write a function to reverse a string
"""def reverse():
    name=input("Name: ").strip().title()
    for i in range(len(name)-1,-1,-1):
      print(name[i],end="")
reverse()"""
#Create a to-do list app (just basic list add/remove/show)
def Todo():
    Task=[]
    print("Welcome to the ToDo app\nyou can perform the following operations.('just basic list add/remove/show)")
    while True:
        print("\n--Menu--")
        print("1️⃣  Add Task")
        print("2️⃣  View Tasks")
        print("3️⃣  Remove Task")
        print("4️⃣  Exit")
        try:
            choice=int(input("Choice: "))
            if choice==1:
                task=input("Task: ").strip().title()
                Task.append(task)
                print(f"Task {task} added to the list.")
            elif choice==2:
                if not Task:
                        print("No task available.")
                else:
                    print("\n-- Show Task--")
                    for task in Task:
                      print(f"Task: {task}")        
            elif choice==3:
                task=input("Task to delete: ").strip().title()
                if  not  Task:
                    print(f"{task} not found in the list.")
                else:
                    for task in Task:
                        Task.remove(task)
                        print(f"Task {task} removed successfully.")
            elif choice==4:
                print("--Exit--")
                print("Thanks for using the ToDo App.")
                break
            else:
                print("Invalid choice. Pleae try again.")
        except ValueError:
            print("Invalid inpit,enter only integer.")
Todo()
    

