"""#🔹 Beginner Level (Basic Operations on Lists & Dictionaries)
#1️⃣ Create a list of names and print each name using a loop.
names=["aiman","ayesha","ali"]
print(names)
names.append("aliya")
print(f"after append: {names}")
names.remove("aiman")
print(f"after remove: {names}")
names.sort()
print(f"after sort: {names}")
for i in range (len(names)):
  print(i+1,names[i])

"""
#6️⃣ Create a dictionary of students with their marks.
"""students=[
 {"Name": "Musfira","Marks":78},
 {"Name": "ayesha","Marks":68},
]
for student in students:
  print(f"Name: {student['Name']}, Marks: {student['Marks']}")"""
#7️⃣ Retrieve and print a student’s marks using their name.
"""students={
  "musfira":98,
  "ayesha":88,
  "aiman":78
}
students['zunaira']=56
students['Aiman']=67
for name, marks in students.items():
  print(f"{name}: {marks}")
name=input("enter name: ")
if name in students:
  print(f"{name} Marks: {students[name]}")
else:
  print(f"student {name} not found.")"""
#Mini project
#contact book
"""contacts={}
def add_contact(name,number):
  contacts[name]=number
  print(f"contact added: {name}-{number} ")
def view_contact():
  if contacts:
    print("\n your contacts")
    for name , number in contacts.items():
      print(f"{name}:{number}")
  else:
    print("No contact found.")
def delete_contact(name):
  if name in contacts:
    del contacts[name]
  else:
    print(f"{name} is not found in {contacts} list.")
  while True:
    print("\n Contacts Books")
    print("1. add contacts")
    print("2. view contacts")
    print("3. delete contacts")
    print("4. exit contacts")
    choice=input("Enter your choice: ")
    if choice=='1':
      add_contact(input("Enter name: "),input("enter number: "))
    elif choice=='2':
      view_contact()
    elif choice=='3':
      delete_contact(input("enter your name to remove: "))
    elif choice=='4':
      print("goodby")
      break
    else:
      print("invalid choice")"""








