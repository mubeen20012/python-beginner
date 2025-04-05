#🔰 Beginner Level (Basic Dictionary Operations)
#Create a dictionary with five key-value pairs representing a student's details (name, age, grade, city, and school).

"""students={
  "ayesha":{"age":23,"Grades":"A+","city":"lahore","school":"city-school"},
   "Ali":{"age":22,"Grades":"A","city":"Karachi","school":"city-school"},
  "Zain":{"age":24,"Grades":"B","city":"lahore","school":"city-school"}
}
#Update the student's grade in the dictionary.
students["ayesha"]["Hobbies"]="reading"
students["ayesha"]["Grades"]="A"
#4️⃣ Delete a Key from Dictionary:
for student in students.values():
  if "city" in student:
    del student["city"]
for name,detail in students.items():
  print(f"Student: {name}")
  for key,value in detail.items():
    print(f"{key}:{value}")
print("\nCountry: ",students.get("country", "not found"))"""
#7️⃣ Merging Two Dictionaries:
"""dict1= {"name":"ali","age":22},
dict2={"subject":"maths","grades":"A"}
merged_dict=dict1 | dict2
print(merged_dict)"""
"""dict1 = {"name": "Ayesha", "age": 22}
dict2 = {"marks": 90, "subject": "Math"}

# Merging using the | operator (Python 3.9+)
merged_dict = dict1 | dict2

print(merged_dict)"""
#🔰 Beginner Level (Basic Dictionary Operations)
#Create a dictionary with five key-value pairs representing a student's details (name, age, grade, city, and school).

"""students={
  "name":"Musfira",
  "age":'22',
  "grade":"A+",
  "city":"Lahore",
  "School":"High School"
}
students["Hobbies"]="reading"
del students["city"]
#print(students["name"])
print(f"country: ", {students.get("country", "not found")})
for key,values in students.items():
  print(f"{key}:{values}")
for key in students:
  print(key)
for values in students.values():
  print(values)"""
#🚀 Intermediate Level (Working with Nested Dictionaries)
#Create a dictionary of students where each key is a student name, and the value is another dictionary containing "age", "marks", and "subject".
students={
  'Ayesha':{"age":'23',"marks":'33',"subject":"Maths"},
  'Aimna':{"age":'24',"marks":'30',"subject":"Maths"},
  'Ali':{"age":'25',"marks":'31',"subject":"Maths"},

}
"""students["Ayesha"]["Hobbies"]="reading"
for student in students:
  if "city" in students:
    del student["city"]
for name,detail in students.items():
  print(f"Name: {name}")
  for key,values in detail.items():
    print(f" {key}:{values}")"""
#7️⃣ Merging Two Dictionaries:
"""dict1={"name":"saira"}
dict2={"subject":"Maths"}
merged_dict= dict1|dict2
print(merged_dict)"""
#8️⃣ Count Word Frequency in a Sentence:
"""def count():
  fruits=["apple","banana","oranges","banana","apple"]
  counts={}
  for fruit in fruits:
    if fruit in counts:
      counts[fruit]+=1
    else:
      counts[fruit]=1
  for fruit,count in counts.items():
    print(f"{fruit}:{count}")
count()"""
#🔰 9️⃣ Dictionary Sorting: Beginner to Intermediate
"""name={"ali":22,"emna":78,"bilal":65}
sorted_dict=dict(sorted(name.items()))
print("sorted by dictionary")
print(sorted_dict)"""
#🔟 Find Maximum & Minimum Values in a Dictionary:
names={'a':10,'b':23,'c':66}
largest=max(names, key=names.get)
smallest=min(names, key=names.get)
print(f"Large: {largest}--{names[largest]}")
print(f"Small: {smallest}--{names[smallest]}")











