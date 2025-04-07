#Day 1: Conditional Logic & Basic Loops
#Daily Problems (10 Questions):
#Write a program that checks if a number is even or odd.
#def function 
"""
def main():
  # take user input
  number=int(input("Enter a number: "))
  even(number)
#  declare function 
def even(num):
#  use conditional to check even or odd
  if num%2==0:
    print(f"{num} is even.")
  else:
    print(f"{num} is odd.")
#call the main function
main()"""
#Write a program that asks the user for their age and prints whether they are eligible to vote.
#def main function
"""def vote():
#  and ask user input
  age =int(input("Enter your age: "))
#  and use condition to check eligible for vote
  if age >=18 and age<90:
    print(f"{age}: your are eligible to vote.")
  elif age >=16 and age <18:
    print(f"{age}: you are teenager and apply for next time.")
  elif age <=90:
    print(f"{age}: you are graet and enter to your jubliee life.")
  else:
    print(f"{age}: you are child.")
#call the main function
vote()"""
#Given a number, print whether it is positive, negative, or zero.
#def function
"""def check_number():
#  take user input 
  number=int(input("Enter a number: "))
# check positive or negative or zero
  if number>0:
    print(f"{number} is positive.")
  elif number <0:
    print(f"{number} is negative.")
  else:
    print(f"{number} is zero.")
#call the main function
check_number()"""
#Ask for two numbers and print which one is larger.
# def main function
"""def larger_number():
#  take user input
  num1=int(input("Enter First number: "))
  num2=int(input("Enter Second number: "))
#  and check the larger number
  if num1>num2:
    print(f"Number {num1} is larger than Number {num2}")
  else:
    print(f"Number {num2} is larger than Number {num1}")
#call the main function
larger_number()"""
#Write a program that asks the user to enter a password and prints “Access Granted” if it matches a preset password, otherwise “Access Denied.”
#def main function 
"""
def password():
#  reset password
   preset_password="3eczja6pq"
#  take user input
   user_pass=input("Enter your password: ") 
   if user_pass==preset_password:
    #and check the password
     print("Access Granted.")
   else:
    print("Access Denied.")
#call the main function
password()"""
#Write a program that prints “Good Morning” if the current hour (simulate with an input) is before 12, else “Good Afternoon.”
"""def greeting():
  hour=int(input("Enter the current hour (0-23): "))
  if hour<12:
    print("Good Morning")
  elif hour <12 and hour<3:
    print("Good Afternoon.")
  else:print("Good evening.")
#call the main function
greeting()"""
#Create a simple grading system: if the score is 90 and above, print “A,” if between 80 and 90, print “B,” etc.
"""def grading_system():
  score=int(input("Enter your Score: "))
  if score >=90:
   print(f"{score} is A+")
   print("Excellent")
  elif score<90 and score>=80:
   print(f"{score} is B")
  elif score <80 and score>=70:
   print(f"{score} is C")
  elif score <70 and score>=60:
   print(f"{score} is D")
  else:
   print(f"{score} is F")
   print("You need more practice.")
grading_system()"""
#Given a day of the week (as input), print whether it is a weekday or weekend.
"""def days_week():
  day=input("Enter a day of week: ").strip().lower()
  if day in ["saturday","sunday"]:
    print(f"{day} is weekend.")
    print("Enjoy your weekend")
  else:
    print(f"{day} is weekday.")
    print("keep work with positive attitude.")
days_week()"""
#Write a program that asks the user to enter a number and then prints “High” if the number is above 50, “Low” if below 50, and “Medium” if equal to 50.
"""def check_number():
  number=int(input("Enter a number: "))
  if number>=80:
    print(f"{number} is High.")
  elif number<80 and number>=60:
    print(f"{number} is Medium.")
  else:
    print(f"{number} is Low.")
check_number()"""
#Ask the user to input a temperature and print “Cold” if below 15, “Warm” if between 15 and 30, and “Hot” if above 30.
"""def weather():
  temp=int(input("Enter the Temperature: "))
  if temp>=30:
    print(f"{temp} is Hot.")
    print("Drink more Water and stay yourself Hydrated.")
  elif temp >=15 and temp<30:
    print(f"{temp} is Warm.")
    print("Enjoy your day.")
  elif temp>10 and temp <15:
    print(f"{temp} is Normal.")
    print("Enjoy Windy Day.")
  else:
    print(f"{temp} is Cold.")
    print("wear warm clothes")
weather()"""
#Mini Project: Basic Calculator
#Task: Build a calculator that can perform addition, subtraction, multiplication, and division.
def Calculator():
  print("\nWelcome to the Mini Calculator")
  while True:
    try:
     num1=float(input("Enter First number: "))
     num2=float(input("Enter Second number: "))
     operator=input("Select the Operator: (+,-,*,/): or q to quit: " ). strip() .lower()
     if operator=='q':
       print("Exit the Calclator.")
       break
     operations={
      '+':num1+num2,
      '-':num1-num2,
      '*':num1*num2,
      '/':num1/num2 if num2!=0 else "Error: Division by Zero"
    }
     print(f"Result: {operations.get(operator, 'invalid operator')}")
    except ValueError:
       print("Error: Invalid Input.")
Calculator()








   













