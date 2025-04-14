#Day 4: Dictionaries & Nested Data
#Daily Problems (10 Questions):
#Create a dictionary with 5 key-value pairs representing a student's details (e.g., name, age, grade, city, school).
"""student={
    "name": "ayesha",
     "age":25,
     "grade": "B",
     "city":"Lahore",
     "school":"Lahore Grammer School"
}
print(student)
#Retrieve and print a student's grade using their name.
print(student["age"])
print(student["name"])
print(student["grade"])
#Update a student's grade.
student["grade"]="A"
print(student["grade"])
#Add a new key-value pair (like "hobbies") to a student's record.
student["hobbies"]="reading"
print(student["hobbies"])
#Delete a key from a student's record (e.g., "city").
del student["city"]
print(student)
#Loop through the dictionary and print each key-value pair.
for key,values in student.items():
    print(f"{key}:{values}")
#Merge two dictionaries.
detail={
    "name":"Ali",
    "age":27
}
student={
    "school": "grammer school"
}
detail.update(student)
print(detail)"""
#Create a nested dictionary where each student name maps to another dictionary with "age", "marks", and "subject".
students={
    "Name":{"Ayesha","Sara","Ali"},
    "Age":{26,27,28},
    "Marks":{65,56,76},
    "Subject":{"Math","Phusis","Computer"},
}
print(students)
#Loop through a nested dictionary to print out all details of each student.
for name,details in students.items():
    print(f"{name}:{details}")
#Use the .get() method to safely retrieve a value from the dictionary.
print(students.get("Name"))
print(students.get(f"{city} city not found"))