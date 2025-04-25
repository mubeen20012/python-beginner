"""#Day 4: Dictionaries 📚
 #Mini Challenges
#Create a dictionary of favorite books (title: author)
Books={
    "Atomic Habits":"J Malan",
     "Mala": "Nimra"
}
#Add new books, update an author, remove a book
Books["Namal"]="Nimra"
Books["peer kamil"]="Humaira"
del Books["peer kamil"]
#Loop through and print formatted output
for title, authors in Books.items():
    print(f"{title}: {authors}")"""
Musfira={
    "Books":{"Atomic Habit": "J Melon"},
    "Hobbies":{"Reading","Coding"}
}
print( Musfira["Books"])
print( Musfira["Hobbies"])
for Books,Hobbies in  Musfira.items():
    print(f"{Books}:{Hobbies}")