#🔥 10 Loop Questions (Beginner to Advanced) with Mini Projects
#✅ Beginner (Basic Concepts)
##1️⃣ Print numbers from 1 to 10 using a loop.
"""for i in range(1,11):
  print(i)
num=int(input("number: "))
for i in range(1,num+1):
  print(i)"""
"""def main():
  num=int(input("number: "))
  number(num)
def number(num):
  n=1
  while n<=num:
    print(n)
    n+=1
main()"""
"""def even():
    number=int(input("number: "))
    num=2
    while num<=number:
        print(num)
        num+=2
even()"""
#3️⃣ Sum of first N numbers (Using While Loop)
"""def sum():
  number=int(input("number: "))
  sum=0
  i=1
  while i<=number:
    sum+=i
    i+=1
  print(f"the sum of {number} is {sum}.")
sum()"""
#4️⃣ Reverse Countdown from N to 1 (Using While Loop)
"""def reverse():
  num=int(input("enter number: "))
  while num>0:
    print(num)
    num-=1
  print("Blast off")
reverse()"""
##6️⃣ Print a Table of a Number (Using For Loop)
"""for i in range(2,11):
  print(f"\nmultiplication table of {i}")
  for j in range(1,11):
    print(f"{i}*{j}={i*j}")"""
#print individual table
"""def table():
  Table=int(input("Table: "))
  print(f"\nMultiplication Table {Table}")
  for i in range(1,11):
    print(f"{Table}*{i}={Table*i}")
table()"""
#4️⃣ Find the factorial of a number (e.g., 5! = 5 × 4 × 3 × 2 × 1).
"""def factorial():
  num=int(input("num: "))
  fact=1
  for i in range(1,num+1):
    fact*=i
  print(f"the factorial of {num} is: {fact}")
factorial()"""
#✅ Intermediate (Using Loops Efficiently)
#6️⃣ Reverse a given number (e.g., 123 → 321).
"""def reverse():
  num=int(input("num: "))
  while num>0:
    print(num)
    num-=1
reverse()"""
#2️⃣ Pattern Printing (Using Nested Loops)
"""def pattern():
  num=int(input("number: "))
  for i in range(1,num+1):
   print("*")
   num-=1
pattern()"""
"""rows=int(input("rows: "))
for i in range(1, rows+1):
  for j in range(i):
    print("*")
  print()"""
#3️⃣ Bank ATM Simulation
balance=1000
while True:
  print("\n1.Check balance \n2.Deposit money\n3.Withdraw money\n4Exit.")
  choice=input("Enter your choice: ")
  if choice=='1':
    print(f"Your Current Balance is ${balance}.")
  elif choice=='2':
    amount=int(input("enter deposited money: "))
    balance+=amount
    print(f"${amount} deposited. your new Balance is: ${balance}")
  elif choice=='3':
    amount=int(input("Enter Withdraw money: "))
    if amount>balance:
      print("insufficent amount")
    else:
      balance-=amount
      print(f"${amount} withdraw. your remaining Balance is: ${balance}.")
  elif choice=='4':
    print("Exit. Thanks")
    break
  else:
    print("invalid choice.")






  


