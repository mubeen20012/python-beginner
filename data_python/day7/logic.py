##Reverse a Number
"""def reverse():
    try:
        number=int(input("Number: ").strip())
        reverse=0
        while number >0:
            digit=number % 10
            reverse= reverse * 10 + digit
            number //=10
        print(f"Reverse: {reverse}") 
    except ValueError:
        print("Invalid Input, allow only integers")
reverse()"""
"""num=[1,2,3]
reverse=num[::-1]
print(reverse)"""
#text
"""name=input("Name: ").strip()
reverse=name[::-1]
print(reverse)"""
"""def reverse():
    text=input("Name: ").strip()
    reverse=''
    for char in text:
        reverse=   char + reverse
    print(f"Reverse: {reverse}")
reverse()"""
"""def number():
    try:
        number =int(input("number: ").strip())
        reverse=0
        while number >0:
            digit= number % 10
            reverse= reverse * 10 + digit
            number //=10
        print(f"Reverse: {reverse}")
    except ValueError:
        print("Invalid Input, allow only integer.")
number()"""
#sum of digits
"""def sum():
    sum=0
    number=[1,2,3,5]
    for num in number:
        sum += num
    print(f"Sum: {sum}")
sum()"""
"""def sum():
    try:
        number=int(input("Number: ").strip())
        sum=0
        while number >0:
          digit=number % 10
          sum=sum + digit
          number //=10
        print(f"Sum: {sum}")
    except ValueError:
       print("Invalid Input, allow only integers.")
sum()"""
#Prime
"""num=29
is_prime=True
if num < 2:
    is_prime=False
else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")
"""
#count vowel
"""def vowel():
    count=0
    word=input("Word: ").strip()
    vowel='AEIOUaeiou'
    for char in word:
        if char in vowel:
            count +=1
    print(f"Count: {count}")
vowel()
"""
#palindrome Check
"""def palindrome():
    word=input("Word: ").strip()
    reverse=word[::-1]
    if word == reverse:
        print(f"This word {word} is palindrome.")
    else:
        print(f"This word {word} is not a palindrome.")
palindrome()"""
##Find Max in a List (without max()).
"""def max():
    list=[]
    for number in range(5):
        try:
          number=int(input("Number: ").strip())
          list.append(number)
        except ValueError:
           print("Invalid Input, allow only integers.")
    largest=list[0]
    for l in list:
       if l > largest:
          largest=l
    print(f"Largest: {largest}")
max()
"""
"""def second():
    list=[]
    for number in range(5):
        try:
          number=int(input("Number: ").strip())
          list.append(number)
        except ValueError:
           print("Invalid Input, allow only integers.")
    largest=second=float('-inf')
    for n in list:
       if n> largest:
          second=largest
          largest=n
       elif n > second and n!= largest:
          second= n
    if second == float('-inf'):
          print("No second largest found.")
    else:
          print(f"Second Largest is: {second}")
second()"""
#fuel guage
"""def guage():
    try:
        fraction=input("Fraction(3/5): ").strip()
        x,y=fraction.split('/')
        x=int(x)
        y=int(y)
        if y==0:
            raise ZeroDivisionError
            
        percentage=round((x/y) * 100)
        if percentage <=1:
            print("E")
        elif percentage >=99:
            print("F")
        else:
            print(f"Percentage: {percentage}%")
    except ValueError:
        print("Invalid Input, allow only integers.")
    except ZeroDivisionError:
        print('Denominator cannot be 0.')
guage()
"""
#Taqueria 🌮
"""def taqueria():
    menu={
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
    for item, price in menu.items():
         print(f"{item} : {price}")
    while True:
     try:
        item=input("Item: ").strip().title()
        total_price=0
        
     except EOFError:
        print()
        break

    if item in menu:
         total_price +=menu[item]
         print(f"Total_Price: {total_price}")
taqueria()
"""
#Grocery List 🛒
def grocery():
    cart=[]
    while True:
        try:
            items=input("Item: ").strip().title()
            cart.append(items)
        except EOFError:
            print()
            break
    print("Grocery List\n")
    for item in cart:
        print(item)
    
    freq={}
    for item in cart:
      if item in freq:
        freq[item] +=1
      else:
        freq[item] =1
    for item in sorted(freq.keys()):
      print(f"Frequency of item:{item}: {freq[item]}")

grocery()
    




    