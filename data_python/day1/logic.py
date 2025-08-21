#🗓️ Day 1 – Basics + Loops + Conditionals
#🧠 2-Hour Logic Building (Pick 5–6)
#✅ Odd or Even Checker
"""def even():
    try:
        number=int(input("Enter Number: ").strip())
        if number%2==0:
            print(f"This {number} number is even.")
        else:
            print(f"This {number} number is odd.")
    except ValueError:
        print("Invalid Input, allow only integers.")
even()"""
#✅ Reverse a String
"""def reverse():
    text=input("Enter Text: ").strip()
    reversed_text=''
    for char in text:
        reversed_text= char + reversed_text
    print(f"Reversed: {reversed_text}")
reverse()"""
#✅ Multiplication Table
"""def table():
    for i in range(2,11):
        print(f"Table is: {i}")
        for j in range(1,11):
            print(f"{i} * {j} = {i * j}")
table()
"""
"""def prime():
    try:
        number=int(input("Enter Number: ").strip())
        if number <=1:
            print(f"Number {number} is not a prime.")
            return
        if number ==2:
            print(f"Number {number} is a prime.")
            return
       
        for i in range(2, int(number ** 0.5)+1):
            if number %i==0:
                print(f"Number {number} is not a prime.")
                return
        print(f"Number {number} is a prime.")
    except ValueError:
        print("Invalid Input,allow only integers.")   
prime()""" 
#🔸 Check Palindrome
"""def palindrome():
    text=input("text: ").strip()
    reverse=text[::-1]
    print(reverse)
    if text==reverse:
        print(f"This {text} is a palindrome.")
    else:
        print(f"This {text} is not a palindrome.")

palindrome()"""
#🔸 Factorial of a Number
"""def factorial():
    try:
        number=int(input("Enter Number: ").strip())
        if number <0:
            print("Number is Less,Factorial is not defined for less number.")
            return
        result=1
        for i in range(1,number+1):
            result *=i
        print(f"Factorial of Number {number} is: {result}")
    except ValueError:
        print("Invalid Input, Allow only integers.")
factorial()"""
def factorial_number():
    try:
        number=int(input("Number: ").strip())
        result=1
        for i in range(1,number +1):
            result *=i
        print(f"The Factorial of number is {number}: {result}")
    except ValueError:
        print("Invalid Input, allow only integers.")
factorial_number()




                    







