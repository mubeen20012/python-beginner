#Inventory Tracker App
def inventory():
    print("\nWelcome to the Inventory Tracker App.")
    Inventory={
        "cream":{"price":900,"Quantity":8},
         "lotion":{"price":100,"Quantity":6}
    }
    print("\n--Menu--")
    print("1. Add New Item")
    print("2.View Item")
    print("3.pdate Quantity of an Item")
    print("4.Remove an Item")
    print("5.Exit")
    while True:
        try:
            choice=int(input("Choice: "))
            if choice==1:
                product=input("Product Name: ").strip()
                price=int(input("Product Price: ").strip())
                quantity=int(input("Product Quantity: ").strip())
                Inventory[product]={"price":price,"quantity":quantity}
                print(f"{product} added Successfully in Inventory.")
            elif choice==2:
                for key, values in Inventory.items():
                   print(f"{key} : {values}")
            elif choice==3:
                product=input("Product Name: ").strip()
                if product not in Inventory:
                    print("Product Not found.")
                else:
                    print("\nProduct found.")
                    for product in Inventory:
                        quantity=int(input("Product Quantity: ").strip())
                        Inventory[product]["quantity"]=quantity
                        print(f"{product} quality updated Successfully")
            elif choice==4:
                product=input("Product Name: ").strip()
                if product not in Inventory:
                    print("Product Not found.")
                else:
                    print("\nProduct found.")
                    for product in Inventory:
                      del Inventory[product]
                      print(f"{product} deleted Successfully.")
            elif choice==5:
                print("---Exit---")
                break
            else:
                print("invalid choice.")       
        except ValueError():
            print("Invalid Input.Allow only integers.")
inventory()
