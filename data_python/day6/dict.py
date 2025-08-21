#🕐 1-Hour Dictionary Practice Plan
#🔹 Beginner (10–15 min)
#Phone Book:
"""def book():
    number={
        'Amina': '923224616539',
        'Ali':   '923224616558',
        'Ayesha': '923224616546',
        'Bilal': '923224616523',
    }
    name=input("Enter Name: ").strip().title()
    if name in number:
        print(f"Number: {number[name]}")
book()"""
#Word Counter:
#Count how many times each word appears in a given sentence.
"""def count():
    count=0
    sentence=''
    word=input("Enter word: ").strip()
    for char in word:
        char += sentence
        count +=1
    print(f"Count: {count}")
count()"""
#Student Grades:
#Store student names and their scores. Print average score.
"""def grade():
    grades={
        'Ayesha' : 50,
        'Amina' : 60,
        'Ali' : 80,
        'Bilal' : 40,

    }
    total=0
    for student,score in grades.items():
        total += score
    average= total /len(grades)
    print(f"Average Score: {average}")
    for student,score in grades.items():
        if score >60:
            print(f"High Score: {student} - {score}")
grade()"""
#Intermediate
#Frequency Counter (Characters):
"""def frequency():
    name=input("Enter Name: ").strip()
    freq={}
    for char in name:
        if char in freq:
          freq[char] +=1
        else:
           freq[char]=1
    print("Character Frequency: ")
    for char,count in freq.items():
       print(f"{char} - {count}")
       
    
frequency()"""
#swap the list
"""def swap():
    number=[1,2,3,4,5,6]
    swap=number[-1:] + number [:-1]
    print(swap)
swap()"""
#Invert Dictionary:
#Swap keys and values of a dictionary. Example: { "a": 1, "b": 2 } → { 1: "a", 2: "b" }.
"""def invert():
    number= { "a": 1, "b": 2 }
    swap={}
    for key,value in number.items():
        swap[value]= key
    print(swap)
invert()"""
#Shopping Cart:
#Dictionary of items and prices. Let the user “buy” items and calculate total cost.
def items():
    cart={
        "cloths" : 700,
        "shoes" : 900,
        "jewellery" : 300,
        "bag" : 600,
    }
    total_price=0

    for cloth, price in cart.items():
        print(f"Cart: {cloth} : {price}")
        total_price += cart[cloth]
    print(f"Total Price: {total_price}")
items()


    
    
