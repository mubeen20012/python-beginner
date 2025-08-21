#Loop Practice Exercises (Beginner → Advanced)
#Beginner
#Repeat a Message: Print "Hello, CS50!" five times using a for loop.
"""def message():
    for i in range(5):
        print("Hello, CS50!")
message()"""
#Even Number Printer: Print even numbers from 2 to 20 using a loop.
"""def even():
    for i in range(2,21):
        if i%2==0:
            print(i)
even()"""
#Word Counter: Given a sentence from user input, count its words by looping through split().
"""def counter():
    count=0
    sentence=''
    word=input("Sentence: ").strip()
    for char in word:
        sentence += char
        count +=1
    print(f"Sentence Count: {count}")
counter()"""
#Intermediate
#List Filter: From a list of numbers, build a new list containing only numbers divisible by 3.
"""def filter():
    list=[]
    number=[1,2,3,9,18,21,4,5]
    for num in number:
      if num %3==0:
         list.append(num)
    print(f"New List: {list}")
filter()"""
#Countdown Timer: Print a countdown from a given positive number n down to 0.
"""def timer():
    number=int(input("Number: ").strip())
    while number >=0:
        print(number)
        number-=1
    
timer()"""
#Reverse String: Reverse a user-input string by building a new string character by character.
"""def reverse():
    name=input("Enter Text: ").strip()
    reverse=''
    for char in name:
        reverse = char + reverse
    print(f"Reversed: {reverse}")
reverse()"""
#Reverse String: Reverse a user-input string by building a new string character by character.
def reverse():
    name=input("Enter Text: ").strip()
    print(name[::-1])
reverse()
