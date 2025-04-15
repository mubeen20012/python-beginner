"""#Day 5: Functions, File Handling & Exception Handling
#Write a function to calculate the factorial of a number.
def factorial():
    number=int(input("Number: "))
    original=number
    fact=1
    while number>1:
        fact*=number
        number-=1  
    print(f"Factorial of {original} is {fact}")
factorial()"""
#Write a function that checks if a number is prime.
"""def is_prime():
    number=int(input("Number: "))
    if number>1:
      for i in range(2,number):
        if number%i==0:
            print(f"{number} is not a prime.")
        else:
           print(f"{number} is a prime.")
    else:
       print(f"{number} is not a prime.")
is_prime()"""
#Write a function that takes a list of numbers and returns only even numbers.
"""def is_even():
    numbers=[1,2,3,4,5,6,7,8,9,10]
    even=0
    for number in numbers:
        if number%2==0:
            even+=number
        print(f"Even numbers are {even}")
is_even()
#Write a function that converts Celsius to Fahrenheit.
def celcius_to_fahrenheit():
    celcius=int(input("Celcius: "))
    fahrenheit=(celcius*9/5)+32
    print(f"Fahrenheit: {fahrenheit}")
celcius_to_fahrenheit()"""
#Write a function to count the number of vowels in a string.
"""def count_vowels():
    string=input("String: ")
    vowels="aeiouAEIOU"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    print(f"The number of vowels in {string} is {count}.")
count_vowels()"""
#Use try-except to handle invalid inputs when converting a string to an integer.
def number():
    try:
        number=int((input("Number: ")))
        if number%2==0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input.please enter a valid input.")
number()
         




