#Week 0 – Practice Problems (Intro to Python)
"""1. Playback Speed
Problem:
Take a string as input and replace every space " " with "...“.

"""
"""def playback():
    text=input("Text: ").strip().title()
    playback=text.replace(" ","...")
    print(f"Playback: {playback}")
playback()"""
"""Making Faces
Problem:
Create a function that replaces emoticons :) with 🙂 and :( with 🙁.
"""
"""def main():
    message=input("Message: ").strip()
    Converted=converted(message)
    print(f"Output: {Converted}")
def converted(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙂")
    return text
main()"""
"""3. Einstein's Formula
Problem:
Ask the user for mass in kilograms and output the equivalent energy using Einstein’s formula:"""
"""mass=int(input("Mass: kg").strip())
c=300000000 
E=mass * c**2
print(f"Energy in joules: {E}")"""
"""def main():
    mass=int(input("Mass: kg").strip())
    E=energy(mass)
    print(f"Energy in joules: {E}")
def energy(mass):
    c=300000000
    E= mass *c**2
    return E
main()"""
#Tip Calculator
#Problem:
"""Ask the user for a bill total and a tip percentage. Calculate and display the tip amount."""
"""def calculator():
    total_bill=int(input("Kindly Enter your bill: $").strip())
    percentage=int(input("How much would you like to tip: ").replace("%",""))
    tip=(total_bill*percentage)/100
    print(f"Your tip is: ${tip}")
calculator()"""
#Say Hello
"""Problem:
Ask the user for their name and print a greeting.
"""
"""name=input("Enter your name: ").strip().title()
print(f"Hy {name}")"""
#6. Simple Calculator
"""def calculator():
   print("Welcome to mini calculator!")
   while True:
      try:
         num1=int(input("Enter first Number: ").strip())
         num2=int(input("Enter second Number: ").strip())
         operator=input("Enter operator(+,-,*,/) or quit: ").strip()
         if operator.lower()=='q':
            print("Exiting------")
            break
         else:
            operation={
               '+': num1 + num2,
               '-': num1 - num2,
               '*': num1 * num2,
               '/': num1 / num2
               if num2!=0 else "Error: Division By Zero"
            }
            print(f"Result: {operation.get(operator,'invalid opearor')}")
      except ValueError:
         print("Invalid input,allow only integer")
calculator()"""
#character counter
"""def counter():
   text=input("Enter Text: ").strip()
   counter=text.replace(" ","")
   print(f"Character Count: {len(counter)}")
counter()"""
#8. Temperature Converter
"""celcius=int(input("Enter temperature in celcius: ").strip())
f=(celcius * 9/5) +32
print(f"Temperature in fehrenheit: {f}")"""
##Even or Odd
"""def even():
    number=int(input("Number: ").strip())
    if number%2==0:
        print(f"Number {number} is even.")
    else:
        print(f"Number {number}is odd.")
even()"""
#positive , negative and zero checker
"""def checker():
    try:
        number=int(input("Number: ").strip())
        if number>0:
            print(f"Number {number} is positive.")
        elif number <0:
            print(f"Number {number} is negative.")
        else:
            print(f"Number {number} is zero.")
    except ValueError:
        print("Invalid input,allow only integers.")
checker()"""
#leap year checker
"""def leap_year():
    try:
        year=int(input("Enter year: ").strip())
        if year %4==0:
            print(f"This year {year} is a leap year.")
        elif year%400==0:
            print(f"This year {year} is a leap year.")
        elif year%100==0:
            print(f"This year {year} is not a leap year.")
        else:
            print(f"This year {year} is not a leap year.")
    except ValueError:
        print("Invalid input,allow only integers.")
leap_year()"""
#✅ 1. Deep Thought
"""def thoughts():
    answer=input("What is the answer to life, the universe, and everything?").strip()
    if answer in ['42','forty-two','forty two']:
        print("yes")
    else:
        print("No")
thoughts()"""
#✅ 2. Home Federal Savings Bank
"""def bank():
    greeting=input("Enter Greeting: ").strip()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
bank()"""
#✅ 4. Math Interpreter
"""def expression():
    try:
        expression=input("Expression(3+4): ").strip()
        x,operator,y=expression.split()
        x=float(x)
        y=float(y)
        if operator=="+":
            result= x+y
        if operator=="-":
            result= x-y
        if operator=="*":
            result= x*y
        if operator=="/":
            if y==0 :
                ("Error: Division by zero")
            else:
                result= x/y
        else:
            print("Invalid operator.")
        print(f"Result: {float(result)}")
    except ValueError:
        print("Invalid input format.")
expression()"""
#FizzBuzz: For numbers 1 to 50:
"""def fizz():
    for i in range(1,50):
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0 or i%5==0:
            print("FizzBuzz")
        else:
            print(i)
fizz()"""
#Reverse a string (without built-in reverse).
"""name=input("Name: ").strip()
reversed=name[::-1]
print(reversed)
"""
"""name=input("Name: ").strip()
reversed= ''
for char in name:
    reversed= char + reversed
print(f"Reversed: {reversed}")"""
#✅ Week 2 – Core Exercises
"""amount_due=50
while amount_due>0:
    try:
        insert_coin=int(input("Insert Coin: ").strip())
        if insert_coin in(5,10,25):
            print("Coin is Valid.")
            amount_due-=insert_coin
            if amount_due>0:
             print(f"Your remaining amount is: {amount_due}")
            elif amount_due==0:
                print("Change owed: 0")
            else:
                change_owed=abs(amount_due)
                print(f"Your change owed: {change_owed} ")
        else:
            print("Coin is not Valid.")
            break
    except ValueError:
        print("Invalid input")"""
"""#🟩 1️⃣ Text Emphasis
sentence=input("Sentence: ").strip()
converted_sentences=sentence.replace(" ","*")
print(converted_sentences)"""
"""import emoji
text=input("Input: ").strip()
output=emoji.emojize(text,language='alias')
print(f"Output: {output}")"""
"""def main():
    text=input("Text: ").strip()
    output=convert(text)
    print(f"Output: {output}")
def convert(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text
main()"""
#Frank, Ian, and Glen’s Letters
"""def string():
    text=input("Text: ").strip()
    converted_string=text.replace(" ","...")
    print(f"Converted: {converted_string}")
string()"""
#4️⃣ Nutrition Facts
"""def nutrition():
    calories={
        "apple": 52,
        "banana": 89,
        "orange": 47,
        "strawberry": 33,
        "grape": 69
    }
    while True:
      fruit=input("Enter fruit name: ").strip().lower()
      if fruit=='exit':
          print("Exiting.....")
          break  
      elif not fruit:
        print("Please enter fruit name.")
      elif fruit in calories:
        print(f"Calories : {calories[fruit]}")
      else:
        print("No fruit found.")
nutrition()"""
#💡 Level 1: Basic Loops & Conditions
#1️⃣ Print all even numbers from 1 to 50.
"""def even():
    for i in range(1,50):
        if i%2==0:
            print("Even")
        else:
            print("odd")
even()"""
#2️⃣ Print the sum of numbers from 1 to 100.
"""def sum():
    sum=0
    for number in range(1,100):
        sum+=number
    print(f"The sum of all number is: {sum}")
sum()"""
#3️⃣ Ask the user for 5 numbers, then print the largest.
"""def largest():
    nums=[]
    for i in range(5):
        while True:
         try:
            number=int(input("Number: ").strip())
            nums.append(number)
            break
         except ValueError:
            print("Invalid input.")
    largest=max(nums)
    print(f"Largest: {largest}")
largest()"""
#4️⃣ Count vowels in a string input.
"""def counter():
    count=0
    string=input("String: ").strip()
    vowels='AEIOUaeiou'
    for char in string:
        if char in vowels:
            count+=1
    print(f"The vowels in: {count}")
counter()"""
#5️⃣ Reverse a string without using [::-1].
"""def reverse():
    text=input("Text: ").strip()
    reversed=''
    for char in text:
        reversed=char + reversed
    print(f"Reversed: {reversed}")
reverse()"""
#💡 Level 2: Intermediate
#6️⃣ Check if a word is a palindrome.
"""def palindrome():
    word=input("Words: ").strip().lower()
    reversed=word[::-1]
    if word==reversed:
        print(f"This word {word} is palindrome.")
    else:
        print(f"This word {word} is not apalindrome.")
palindrome()"""
#7️⃣ Create a multiplication table for a given number (up to 10).
"""def table():
    table=int(input("Table: ").strip())
    print(f"Multiplication Table of {table}: ")
    for j in range(1,11):
        print(f"{table} * {j} = {table * j}")
table()"""
"""def table():
    for i in range(2,21):
        print(f"\nMultiplication Table of {i}: ")
        for j in range(1,11):
          print(f"{i} * {j} = {i * j}")
table()   """ 
#8️⃣ Ask for a sentence and print each word on a new line.
"""def split():
    sentence=input("Sentence: ").strip()
    sentences=sentence.split()
    for sentence in sentences:
        print(f"Split Sentences: {sentence}")
split()
"""
"""def split():
    sentence=input("Enter sentence: ").strip()
    sentences=sentence.split()
    for sentence in sentences:
        print(f"Split sentences: {sentence}")
split()"""
#Print Fibonacci numbers up to N terms.
"""def fibonacci():
    term=int(input("Enter the number of term N: ").strip())
    a=0
    b=1
    count=0
    while count< term:
        print(a)
        c= a+b
        a=b
        b=c
        count+=1
fibonacci()"""
#🔟 Simulate a simple login (3 attempts to enter the correct password).
"""def password():
    correct_password="musfira445"
    for attempt in range(3):
        password=input("Password: ").strip()
        if password==correct_password:
            print("Access Granted.")
            break
        else:
            print("Password is incorrect.")
    else:
        print("Access Denied,Too many correct attempt.")
password()"""
#1️⃣ Print all prime numbers between 1 and 100.
"""def prime():
    for number in range(2,101):
        is_prime=True
        for i in range(2,number):
            if number%i==0:
                is_prime=False
        if is_prime:
            print(number)
prime()
"""
##3️⃣ Count the frequency of each character in a string
"""def frequency():
    freq={}
    text=input("Text: ").strip()
    for t in text:
        freq[t]=freq.get(t,0) +1
    for char,count in freq.items():
        print(f"{char} : {count}")
frequency()"""
##4️⃣ Remove duplicates from a list of numbers
"""number=input("Number: ").strip()
list=[]
for n in number:
    if n not in list:
        list.append(n)
print(f"Unique: {list}")"""
"""import requests
response=requests.get("https://api.ipify.org?format=json")
print(response.headers['content-type'])
data =response.json()
#print(data)
print(f"Your IP address is: {data['ip']} ")
"""
"""import requests
city=input("Enter City Name: ").strip().title()
url=f"https://wttr.in/{city}?format=3"
response=requests.get(url)
print(response.headers['content-type'])
print("Weather Report:")
print(response.text)"""
#Random Joke Generator
"""import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
print(response.headers['content-type'])
data=response.json()
print(data['type'])
print(data['setup'])
print(data['punchline'])
print(data['id'])"""
"""import requests
while True:
    try:
        url="https://official-joke-api.appspot.com/random_joke"
        response=requests.get(url)
        data= response.json()
        print(data['type'])
        print(data['setup'])
        print(data['punchline'])
        print(data['id'])
    except ValueError:
        print("Went something wrong, check your interne connection")
    again=input("If you want to agin: ").strip().lower()
    if again!= "yes":
        print("Thank you so much\nExiting-----")
        break
        """
"""import emoji
user=input("Enter sentence: ").strip()
converted=emoji.emojize(user, language='alias')
print(f"Hello: {converted}")"""
# 2. Adieu, Adieu
"""def adieu():
    names=[]
    while True:
        try:
            name=input("Enter name: ").strip().title()
            names.append(name)
        except EOFError:
            print()
            break
    if len(names)==1:
        print(f"Adieu, {names[0]}")
    elif len(names)==2:
        print(f"Adieu, {names[0]} and {names[1]}")
    else:
        formatted=", ".join(names[:-1]) + f", and {names[-1]}"
        print(f"Adieu, {formatted}")
adieu()
"""
# 1. Shopping List Formatter 🛒
"""def shopping():
    cart=[]
    while True:
        try:
            grocessary=input("You need to buy: ").strip().title()
            cart.append(grocessary)
        except EOFError:
            print()
            break
    if len(cart)==1:
        print(f"Itmes: {cart[0]}")
    elif len(cart)==2:
        print(f"Itmes: {cart[0]} and {cart[1]}")
    else:
        formatted=", ".join(cart[:-1]) + f" ,and {cart[-1]}"
        print(f"Cart, {formatted}")
shopping()"""
#Name List to Birthday Invite 🎉
"""def bithday():
    birthday_list=[]
    while True:
        try:
            Guest_name=input("Guest_names: ").strip().title()
            birthday_list.append(Guest_name)
        except EOFError:
            print()
            break
    if len(birthday_list)==1:
        print(f"You are Inviting: {birthday_list[0]}")
    elif len(birthday_list)==1:
        print(f"You are Inviting: {birthday_list[0]} and {birthday_list[1]}")
    else:
        formatting=", ".join(birthday_list[:-1]) + f" and {birthday_list[-1]}"
        print(f"You are Inviting: {formatting}")
bithday()
"""
#🔹 3. Frank, Ian, and Glen's Letters
"""def frank():
    ask=input("say something: ").strip()
    converted=ask.replace(" ","....")
    print(f"Your Output: {converted}")
frank()"""
#🔹 4. Guessing Game
import random
import sys
if len(sys.argv)< 3:
    print("Kindly enter your name first")
else:
    name=sys.argv[1]
    number=int(sys.argv[2])
    print(f"Your name is {name} and number is {number}")
    print("Welcome to the Number guessing game!\nI am thinking the number between i to 100.")
    difficulty=input("Choose difficulty: (easy/hard)").strip().lower()
    if difficulty=='easy':
        max_range=20
    elif difficulty=='hard':
        max_range=100
    secret=random.randint(1,max_range)
    attempt=0
    while True:
        try:
            guess=int(input("Guess: ").strip())
            attempt+=1
            if guess < secret:
                print("Too Low\nTry again")
            elif guess > secret:
                print("Too High\nTry again")
            else:
                print(f"Congratulation! You guess The correct number {secret} aftre {attempt} attempts.")
                play_again=input("If you want to play again: ").strip().lower()
                if play_again!= "yes":
                    break
                else:
                    secret=random.randint(1,max_range)
                    attempt=0 
            if attempt==7:
                    print(f"❌ Game Over! You've used all 7 attempts. The correct number was {secret}.")
                    break
        except ValueError:
            print("Invalid Input, Try again")














    












        

 






    

























    









