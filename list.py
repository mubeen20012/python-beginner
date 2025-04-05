#🔥 10 List Problems (Beginner to Advanced) with a Mini-Project
#✅ Beginner (Basic List Operations)
#1️⃣ Create a list of 5 numbers and print each number using a loop.
"""numbers=[1,2,3,4,5]
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
def remove_duplicate(input_list):
  unique_list=[]
  for item in input_list:
    if item not in unique_list:
      unique_list.append(item)
  return unique_list
original_list=[1,2,2,3,4,4]
result=remove_duplicate(original_list)
print(f"duplicate: {result}")





