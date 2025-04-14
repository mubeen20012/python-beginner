#Mini Project: Contact Book
def contact_book():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    contact_book={}
    while True:
     try:
        choice=int(input("Enter your choice: "))
        if choice==1:
            name=input("Enter name: ")
            phone=int(input("Number: "))
            contact_book[name]=phone
            print("Contact addedd Successfully.")
        elif choice==2:
           for name,phone in contact_book.items():
              print("__Displaying Contact__")
              print(f"Name:{name}")
              print(f"Phone Number: {phone}")
              if not contact_book:
                 print("Contact Book is empty.")
        elif choice==3:
            name=input("Enter name to search: ")
            if name in contact_book:
               print(f"Contact found: {phone}")
            else:
               print("Contact not found.")
        elif choice==4:
            name=input("Enter name to delete: ")
            if name in contact_book:
               del contact_book[name]
               print("Contact deleted Successfully.")
            else:
               print("Contact not Found.")
        elif choice==5:
           contact_book["email"]="musfiramubeen@gmail.com"
           print("Email added Successfully.")
        elif choice==6:
           print("Exiting---")
           break
        else:
           print("Invalid choice.")
     except ValueError:
        print("invalid input.")
contact_book()


           




