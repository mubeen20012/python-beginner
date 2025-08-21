#🧠 2-Hour Logic Building Tasks
#Find Max in a List
"""highest=[]
numbers=[2,3,4,5,6,7,8]
for num in numbers:
    highest.append(num)
highest=max(highest)
print(highest)"""
"""def max():
    numbers=[1,4,5,7,3]
    highest=numbers[0]
    for num in numbers:
        if num > highest:
            highest= num
    print(f"Highest Number is: {highest}")
max()"""
#Sum of List Elements
"""def sum():
    sum=0
    numbers=[3,5,6,2,7,9]
    for num in numbers:
        sum+=num
    print(f"Sum of Number is: {sum}")
sum()"""
#Remove Duplicates from List
"""def duplicate():
    unique=[]
    number=[2,4,2,4,5,8,1]
    for num in number:
        if num not in unique:
           unique.append(num)
    print(unique)
duplicate()"""
#Count Frequency of Each Element
"""def frequency():
    fre={}
    numbers=[2,3,4,6,7,8,2,3,7]
    for num in numbers:
        if num in fre:
            fre[num] +=1
        else:
            fre[num]=1
    print(fre)
frequency()"""
#Check if a List is Palindrome
"""def palindrome():
    names=['musfira','level']
    for word in names:
        reverse_word=word[::-1]
        if word==reverse_word:
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")
palindrome()"""
"""num1=[1,2,3]
num2=[4,5,6]
number=num1 + num2
print(number)
"""
#⏳ 1-Hour Loop Practice – Harvard Style
#1️⃣ Multiplication Table
"""def table():
    for i in range(2,11):
        print(f"\nMultiplication Table of: {i}\n")
        for j in range(1,11):
            print(f"{i} * {j} = {i * j}")
table()
"""
#stars Pattern
"""def star():
    star=int(input("Stars: ").strip())
    for i in range(1,star+1):
        print("*" * i)
star()"""
#Grocessory List
def list():
    items={}
    while True:
        try:
            item=input("Items: ").strip().upper()
            if item in items:
                items[item] +=1
            else:
                items[item] =1
        except EOFError:
            print()
            break
    for item in sorted(items.keys()):
       print(f"{items[item]} {item}")
list()







