#🗂️ Contact Book - Project
def contacts():
  contacts={}
  print("\nContact Book")
  print("__Main Menu__")
  print("1.Add new Contact.")
  print("2.View All Contact.")
  print("3.Search Contact by Name.")
  print("4.Update  Contact.")
  print("5.Delete Contact.")
  print("6.Exit.")
  while True:
   try:
    choice=int(input("Choice: "))
    if choice==1:
      name=input("Name: ").title().strip()
      phone=int(input("Phone: ").strip())
      mail=input("Mail: ").title().strip()
      contacts[name]={"phone":phone, "mail":mail} 
      print(f"{name} added Successfully.")
    elif choice==2:
      if  not contacts:
         print("No contact found.")
      else:
         print("Content found.")
         for name, details in contacts.items():
            print("\n__Display contact__")
            print(f"Name:{name}")
            print(f"Phone:{details["phone"]}")
            print(f"Email:{details["mail"]}")
    elif choice==3:
         name=input("Name: ").title().strip()
         if name in contacts:
            details=contacts[name]
            print("contact found.")
            print(f"Name: {name}")
            print(f"Phone: {details["phone"]}")
            print(f"Mail: {details["mail"]}")
         else:
            print("contact not found.")
    elif choice==4:
         name=input("Name: ").title().strip()
         if name in contacts:
            print("contact found.")
            print("__history of contact__")
            print(f"Name: {name}")
            print(f"Phone: {details["phone"]}")
            print(f"Mail: {details["mail"]}")
            phone=int(input("Phone: ").strip())
            mail=input("Mail: ").title().strip()
            contacts[name]={"phone": phone, "mail": mail}
            print(f"{name} updated successfully.")
         else:
            print("This name is not in contact list.")
    elif choice==5:
         name=input("Name: ").title().strip()
         if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully.")
         else:
            print(f"{name} not in contact list.")
    elif choice==6:
             print("Exit----")
             break
    else:
      print("Invalid choice.")
   except ValueError:
      print("Invalid input.please enter a number.")
contacts()




               
                  




              



