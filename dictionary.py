#Lists - Beginner Level
#Create a list of numbers and write a function to find all even numbers in the list.
"""def find_even():
  numbers=[1,2,3,4,5,6,7,8,9,10]
  even_numbers=[]
  for number in numbers:
    if number%2==0:
      even_numbers.append(number)
      print(f"the even number are {even_numbers}")
find_even()"""
#Problem 2: Find common elements between two lists
"""num1=[1,2,3,4,5,6]
num2=[2,4,6,8,10,7]
num3=[]
for item in num1:
  if item in num2:
    num3.append(item)
    print(f"common element in {num3}")"""
#2️⃣ Find the sum and average of all numbers in a list.
"""numbers=[1,2,3,4,5]
sum=0
for number in numbers:
  sum+=number
average=sum/len(numbers)
print(f"sum: {sum}")
print(f"average: {average}")
#3️⃣ Reverse a list without using the built-in .reverse() method.
numbers=[6,5,4,3,2,1]
for i in range(len(numbers)-1,-1,-1):
  print(numbers[i])
#4️⃣ Find the largest and smallest numbers in a list.
numbers=[56,67,34,99]
smallest=numbers[0]
largest=numbers[0]
for number in numbers:
  if number< smallest:
    smallest=number
  if number>largest:
    largest=number
print(f"smallest: {smallest}")
print(f"largest: {largest}")
#🔥 10 List Problems (Beginner to Advanced) with a Mini-Project
#✅ Beginner (Basic List Operations)
#1️⃣ Create a list of 5 numbers and print each number using a loop.
numbers=[1,2,3,4,5]
for number in numbers:
  print(number)"""
#2️⃣ Find the sum and average of all numbers in a list.
"""number=[10,20,35,47,54]
total=0
for num in number:
  total+=num
average=total/len(number)
print(f"sum: {total}")
print(f"average: {average}")"""
#3️⃣ Reverse a list without using the built-in .reverse() method.
"""num=[7,6,5,4,3,2,1]
for i in range (len(num)-1,-1,-1):
  print(num[i])
#4️⃣ Find the largest and smallest numbers in a list.
numbers=[55,34,78,56]
smallest=numbers[0]
largest=numbers[0]
for num in numbers:
  if num>largest:
    largest=num
  if num<smallest:
    smallest=num
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")"""
#5️⃣ Remove duplicates from a list without using set().
"""def remove_duplicate(input_list):
  unique_list=[]
  for item in input_list:
    if item not in unique_list:
      unique_list.append(item)
  return unique_list
original_list=[1,2,2,3,4,4]
result=remove_duplicate(original_list)
print(f"duplicate: {result}")"""
#🌟 Advanced Mini-Project
#🔟 Todo List Application
def Todo_application():
  tasks=[]
  print("\nWelcome to Todo Application!")
  print("\n1.Add Task")
  print("\n2.View Task")
  print("\n3.Remove Task")
  print("\n4.Exit Task")
  while True:
    choice=input("Enter your choice: ")
    if choice=='1':
      task=input("add task: ")
      tasks.append(task)
      print(f"your {task} is added.")
    elif choice=='2':
      if not  tasks:
         print("no task available.")
      else:
       for task in tasks:
         print(f"-{task}")
    elif choice=='3':
      task=input("enter task to remove: ")
      if task in tasks:
        tasks.remove(task)
        print(f"Task {task} is removed.")
      else:
        print("task not found.")
    elif choice=='4':
      print("thanks")
      break
    else:
      print("Invalid choice,Try again.")
Todo_application()
  
#Allow the user to add, remove, and view tasks.

#Store tasks in a list and loop through it for display.

#Include an option to mark tasks as completed.










  
     





