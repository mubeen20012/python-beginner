#🔹 Step 3: Mini Challenges (20%)
#Conditions: Build a program that checks whether a password is strong.
"""password=input("enter password: ")
if len(password)<8:
  print("Week password")
elif len(password)>10:
  print("Too much")
else:
  print("strong password")"""
#Loops: Print a multiplication table for a given number.
"""for i in range(2,11):
  print(f"\nMultiplication Table")
  for j in range(1,11):
    print(f"{i}*{j}={i*j}")"""
#Lists/Dictionaries: Store and search student marks.
names=["ayesha","amina",'ali']
names.append("aiman")
print(f"after append: {names}")
names.remove("ali")
print(f"after removal: {names}")
names.sort()
print(f"after Sorted: {names}")
for name in names:
  print(name)
for i in range (len(names)):
  print(i+1,names[i])
#dictionaries
students={
  "name":"ayesha","Marks":89,
  "name":"amina","Marks":79,
}
for name,Marks in students.items():
  print(f"{name}:{Marks}")



  