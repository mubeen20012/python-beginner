#beginner project
#mini calculator
"""def calculator():
  print("\nWelcome to mini calculator.\nperform basics operations.")
  while True:
    try:
      num1=float(input("First number: "))
      num2=float(input("Second number: "))
      operator=input("Select operatons('+','-','*','/','%')or 'q'to quit: ")
      if operator.lower()=='q':
        print("Existing Calculator! Good by")
        break
      operations={"+":num1+num2,"-":num1-num2,"*":num1*num2,"/":num1/num2 if num2!=0 else"Error: Division by zero"} 
      print(f"Result: {operations.get(operator,'invalid operator!')}")
    except ValueError:
      print("Error: Invalid input,please enter numbers.")
calculator()"""
#📝 Mini-Project: "Number Guessing Game"
import random
"""def number_guessing_game():
  number=random.randint(1,100)
  guess=None
  attempts=0
  print("\nWelcome to the number guessing game!")
  print("Select the numebr between(1,100)")
  while True:
    try:
      guess=int(input("Guess: "))
      attempts+=1
      if guess<number:
        print("Too low,Try again.")
      elif guess>number:
        print("Too high,Try again.")
      else:
        print(f"Congratulation! you guess the {number} after {attempts} attempt.")
        break
    except ValueError:
      print("invalid input!")
number_guessing_game()"""
#📌 Day 3: Lists & Tuples
#💡 Coding Exercises:
#✅ Find the sum and average of numbers in a list.
"""numbers=[1,2,3,4,5]
sum=0
for number in numbers:
  sum+=number
average=sum/len(numbers)
print(f"Sum: {sum}")
print(f"average: {average}")"""
#✅ Find the largest and smallest numbers in a list.
"""numbers=[88,99,33,65]
smallest=numbers[0]
largest=numbers[0]
for number in numbers:
  if number>largest:
    largest=number
  if number<smallest:
    smallest=number
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")"""
#✅ Reverse a list without using .reverse().
"""numbers=[6,4,3,2,1]
for i in range(len(numbers) -1,-1,-1):
 print(numbers[i])"""
#✅ Remove duplicates from a list without using set().
"""def duplicate():
 list=[1,2,2,3,4,5,4]
 new=[]
 for item in list:
  if item not in new:
   new.append(item)
  print(f"duplicate: {new}")
duplicate()"""
#📝 Mini-Project: "To-Do List App"
"""def Todo_list():
 tasks=[]
 print("\nWelcome to the Todo App")
 print("1.Add Tasks")
 print("2.View Tasks")
 print("3.Remove Tasks")
 print("4.Exit")
 while True:
  choice=input("Enter Choice: ")
  if choice=='1':
    print("\nKindly add Tasks")
    task=input("Tasks: ")
    tasks.append(task)
    print("Added Tasks")
  elif choice=='2':
    if not tasks:
      print("Task not available.")
    for task in tasks:
      print("\nYour Tasks")
      print(f"-{task}")
  elif choice=='3':
    task=input("enter task to remove: ")
    if task in tasks:
      tasks.remove(task)
      print("Task removed successfully.")
    else:
       print("This task is not in tasks.")
  elif choice=='4':
    print("GoodBy")
    break
  else:
    print("Invalid Choice.")

Todo_list()"""
#✅ 1️⃣ Contact Book (Basic CRUD - Create, Read, Update, Delete)
contact_books={}
contact_books={
 "aimna":{"contact":'923224616539',"Email": "aminamubeen553@gmail.com"},
 "ayesha":{"contact":'92322671354',"Email": "ayeshaasgher453@gmail.com"}
}
contact_books["ayesha"]["House"]="Lahore"
contact_books["aimna"]["House"]="karachi"

print("\nDisplay")
for name,detail in contact_books.items():
  print(f"Name: {name}")
  for key,values in detail.items():
    print(f"{key}:{values}")
#search name
search_name="aimna"
if search_name in contact_books:
  print(f"\nFound {search_name} in contacts")
  for key,values in contact_books[search_name].items():
    print(f"{key}:{values}")
else:
    print(f"\n Not Found {search_name} in contacts")
print(f"\nCheck unknown contacts")
print(f"Ali: ,{contact_books.get("Ali","Not Found")}")



   







  