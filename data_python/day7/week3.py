#📘 2 Hours Harvard CS50P Week 3 – Problem Set
#✅ PSet 3 Exercises
"""def fuel_guage():
    try:
        fraction=input("Fraction: ").strip()
        x,y=fraction.split('/')
        x=int(x)
        y=int(y)
        if y==0:
            raise ZeroDivisionError
        percentage=round ((x/y) * 100)
        if percentage <=1:
            print("E")
        elif percentage >=99:
            print("F")
        else:
            print(f"{percentage}%")
    except ValueError:
        print("Invalid Input,allow only Integers.")
    except ZeroDivisionError:
        print("Denominator cannot be zero.")

fuel_guage()
"""
#Taqueria
"""def taqueria():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    while True:
     try:
      total_price=0
      item=input("Enter Items: ").strip().title()
      if item in menu:
        total_price += menu[item]
        print(f"Total: ${total_price:.2f}")
      else:
        pass
      
     except EOFError:
       print()
       break
     
taqueria()"""
#Grocery List 🛒
"""def grocery():
    cart=[]
    while True:
        try:
            items=input("item: ").strip().title()
            cart.append(items)
        except EOFError:
            print()
            break
    for item in cart:
      print(f"Cart: {item}")
grocery()"""
"""def grocery():
    cart={}
    while True:
        try:
            item=input("item: ").strip().lower()
           
            if item in cart:
                cart[item] +=1
            else:
                cart[item] =1


        except EOFError:
            print()
            break
    for item in sorted(cart.keys()):
        print(f"{cart[item]} {item.upper()} ")

grocery()
"""
#Outdated 📅
def outdated():
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:  # Numeric format M/D/YYYY
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)

            else:  # Text format: Month D, YYYY
                parts = date.replace(",", "").split()
                if len(parts) != 3:   # make sure exactly 3 parts
                    raise ValueError
                month_name, day, year = parts
                month = months[month_name]
                day, year = int(day), int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02d}-{day:02d}")
                break

        except (ValueError, KeyError):
            print("Invalid date, try again...")

outdated()



      
     
