#🔄 10 Loop Practice Questions (Beginner → Advanced)
#🔄 10 Loop Practice Questions (Beginner → Advanced)
#Print numbers from 1 to 10 using a for loop.
"""def number():
    for number in range(1,11):
        print(number)
number()"""
#Print the multiplication table of 5 (from 1 to 10).
"""def table():
    table=int(input("Table Number: ").strip())
    print(f"\nTable Number {table}:\n ")
    for j in range(1,11):
        print(f"{table} * {j} = {table * j}")
table()"""
"""def table():
    for i in range(2,11):
        print(f"\nTable is {i}: \n" )
        for j in range(1,11):
            print(f"{i} * {j} = {i * j}")
table()"""
#Sum all numbers from 1 to 100 using a loop.
"""def sum():
    sum=0
    for number in range(1,101):
        sum +=number
    print(f"Sum of all number is: {sum}")
sum()"""
#Count how many vowels are in a given string.
"""def vowel():
    count=0
    text=input("Text: ").strip()
    vowel='AEIOUaeiou'
    for char in text:
        if char in vowel:
            count +=1
    print(f"Vowel Count: {count}")
vowel()"""
#Given a list of names, print each name on a new line.
"""names = ["Ali", "Sara", "Omar"]
for name in names:
    print(name)"""
#Intermediate
#Given a list of integers, print only the even numbers.
"""def list():
    numbers=[1,2,3,4,5,6,7,8,9,12,13,14]
    for num in numbers:
        if num%2==0:
            print(num)
list()"""
#Reverse a string using a loop.
"""def reverse():
    text=input("Say Something: ").strip()
    reverse=text[::-1]
    print(f"Reverse: {reverse}")
reverse()"""
"""def reverse():
    text=input("Say Something: ").strip()
    reverse=''
    for char in text:
        reverse= char + reverse
    print(f"Reverse: {reverse}") 
reverse()"""
#Print the first 10 Fibonacci numbers using a loop.
n=10
a,b=0,1
for i in range(n):
    print(a, end=' ')
    a,b = b, a+b


