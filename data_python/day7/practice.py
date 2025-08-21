#🔟 Logic Building Questions (1 Hour)
#Reverse a Number
"""def number():
    try:
        number=int(input("Enter Number: ").strip())
        reverse=0
        while number >0:
            digit=number %10
            reverse=reverse *10 + digit
            number//=10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input, allow only Integers.")
number()"""
"""def number():
    try:
        num=int(input("Number: ").strip())
        reverse=0
        while num >0:
            digit=num%10
            reverse= reverse *10 + digit
            num //=10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input,allow only integers.")
number()"""
#Sum of Digits
"""def sum():
    sum=0
    try:
        number=int(input("Number: ").strip())
        while number >0:
          digit= number %10
          sum+=digit
          number//=10
        print(f"Sum: {sum}")
    except ValueError:
        print("Invalid Input, allow only Integers.")
sum()"""
#prime
"""num=29
is_prime=True
if num <2:
    is_prime= False
else:
    for i in range(2,num):
        if num %i==0:
            is_prime=False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")"""
#Count Vowels
#Input: "harvard python" → Output: 4.
"""def vowel():
    count=0
    sentence=input("Sentence: ").strip()
    vowel='AEIOUaeiou'
    for char in sentence:
        if char in vowel:
            count +=1
    print(f"Count: {count}")
vowel()"""
#Palindrome Check
"""def palindrome():
    text=input("Text: ").strip()
    reverse=text[::-1]
    if text == reverse:
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")


palindrome()"""
#Find Max in a List (without max()).
"""def largest():
    largest=[]
    for i in range(5):   
      try:
        number=int(input("Number: ").strip())
        largest.append(number)
      except ValueError:
        print("Invalid Input,allow only integer.")
    largest=max(largest)
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    numbers=[]
    for i in range(5):   
      try:
        number=int(input("Number: ").strip())
        numbers.append(number)
      except ValueError:
        print("Invalid Input,allow only integer.")
    largest=numbers[0]
    for n in numbers:
       if n > largest:
          largest=n
    print(f"Largest: {largest}")
largest()
"""
#Second Largest Number in a list.
def second_largest():
    numbers=[]
    for i in range(5):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid input, allow only integers")
    largest=second=float('-inf')
    for n in numbers:
        if n > largest:
            second=largest
            largest=n
        elif n > second and n != largest:
            second = n
    if second == float('-inf'):
        print("No second largest found (all numbers may be same).")
    else:
        print(f"Second Largest number is: {second}")
second_largest()





