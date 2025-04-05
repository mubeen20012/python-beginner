#🔹 Step 1: Conditions (if-else) – 10 Questions
#Beginner:
#1️⃣ Write a program that checks if a number is even or odd.
#create a own function
"""def main():
  #take user input
  number=int(input("Enter number: "))
  #declare own function
  even(number)
def even(num):
  #use conditional
  if num%2==0:
    print(f"{num} is Even.")
  else:
    print(f"{num} is Odd.")
main()"""
#2️⃣ Ask the user to enter their age. If age is 18 or above, print "You can vote"; otherwise, print "You cannot vote".
#def function
"""def main():
  #take input
  try:
    age=int(input("Enter your age: "))
    vote(age)
#  declare own function 
def vote(n):
# use conditional and print
     if n>=18:
       print(f"{n} is eligible for vote.")
     elif n<18 and n>=12:
       print(f"{n} you are a teenager.")
     else:
       print(f"{n} you cannot vote.")
  except ValueError:
     print("enter only integers.")
main()"""
#3️⃣ Check if a given number is positive, negative, or zero.
#take input as a number
"""number=int(input("Enter number: "))
#use conditional to check number
if number>0:  #input >0:positive
   print(f"{number} is Positive.")
elif number<0: #input <0: negative
   print(f"{number} is Negative.")
else:      # input =0: 0
  print(f"{number} is Zero.")"""
#4️⃣ Ask for two numbers and print the greater one.
# take input
"""def Compare_number():
  try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
#  declare own function use conditional
    if num1>num2:
     print(f"{num1} is greater than {num2}.")
    elif num2>num1:
     print(f"{num2} is greater than {num1}.")
    else:
     print(f"{num1} and {num2} both equal.")
  except ValueError:
    print("enter valid correct number.")
Compare_number()"""

     




