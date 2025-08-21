#10 Extra Loop Logic-Building Questions (Beginner → Advanced)
#Beginner
#Print all odd numbers between 1 and 20.
"""def checker():
    for number in range(1,21):
        if number%2!=0:
            print(number)
checker()"""
#Print numbers from 10 down to 1.
"""for number in range(1,11):
    print(number)"""
"""def number():
    n=10
    while n >0:
        n-=1
        print(n)
number()"""
#Ask the user for a number n and print the sum of all numbers from 1 to n.
"""def sum():
    sum=0
    try:
      number=int(input("Enter Number: ").strip())
      for i in range(1,number):
         sum+=i
      print(f"Sum of all Number is: {sum}")
    except ValueError:
       print("invalid input, allow only integers.")
sum()"""
#Print the square of each number from 1 to 10.
"""def square():
    for number in range(1,11):
        square=number **2
    print(f"Square of all number is: {square}")
square()"""
#Ask the user for a word and print each letter on a new line.
"""def word():
    words=input("Enter word: ").strip()
    for char in words:
        print(char)
word()        
"""
#Intermediate
#Count how many consonants are in a given string.
"""def consonants():
    count=0
    word=input("Enter word: ").strip()
    vowel='AEIOUaeiou'
    for char in word:
        if char not in vowel:
            count+=1
    print(f"Constants: {count}")
consonants()"""
#Find the largest number in a list without using max().
"""def largest():
    largest=[]
    numbers=[1,2,3,4,5,6,7,8,9]
    for num in numbers:
        largest.append(num)
    largest=max(largest)
    print(f"Largest number is: {largest}")
    
largest()"""
#Given a number, check if it’s prime using a loop.
"""def prime():
    number=int(input("Enter Number: ").strip())
    if number <2:
        print(f"{number} is not a prime number.")

    for d in range(2,number):
        if number % d==0:
            print(f"{number} is not a prime number.")

    print(f"{number} is a prime number.")
prime()"""
#Print a pattern:
def star():
    star=int(input("Star: ").strip())
    for i in range(1,star):
        print("*" * i)
star()


