#📝 List Practice Exercises (Beginner → Advanced)
#🔹 Beginner (Basics & Accessing)
#Create a list of 5 fruits and print the first and last fruit.
"""def fruit():
    fruits=['apple','banana','mango','grapes','peach']
    print(fruits[0])
    print(fruits[-1])
fruit()"""
#Add "Mango" to a fruit list and remove "Apple".
"""def fruit():
    
    fruits=['apple','banana','grapes','peach']
    fruits.append('mango')
    fruits.remove('apple')
    print(fruits)
    
fruit()"""
#Find the length of a list of numbers.
"""def fruit():
    
    fruits=['apple','banana','grapes','peach']
    print(len(fruits))
    
fruit()"""
#Given a list [2, 4, 6, 8, 10], print the 3rd element.
"""def number():
    number=[2, 4, 6, 8, 10]
    print(number[2])
number()"""
#Reverse a list using slicing ([::-1]).
"""def number():
    number=[2, 4, 6, 8, 10]
    print(number[::-1])
number()"""
#🔹 Intermediate (Looping & Conditions)
#Print each item of a list of names on a new line.
"""def fruit():
    fruits=['apple','banana','grapes','peach']
    for fruit in fruits:
        print(fruit)
fruit()"""
#Given [1,2,3,4,5,6,7,8,9], create a new list with only even numbers.
"""def even():
    even=[]
    number=[1,2,3,4,5,6,7,8,9]
    for num in number:
        if num%2==0:
            even.append(num)
    print(f"Even: {even}")
even()"""
#Count how many times "Ali" appears in a list of names.
"""def name():
    count=0
    names=["Ali","Ayesha",'Amina',"Ali","Ali"]
    for name in names:
        if name =='Ali':
            count +=1
    print(f"Ali Appear: {count}")
name()"""
#Remove duplicates from a list: [1,2,2,3,4,4,5].
"""def duplicate():
    duplicate=[]
    number=[1,2,2,3,4,4,5]
    for num in number:
        if num not in duplicate:
            duplicate.append(num)
    print(f"Duplicate: {duplicate}")
duplicate()"""
#Sort a list of numbers in ascending and descending order.
"""def ascending():
    number=[4,3,2,5,7,4,2,1]
    print(sorted(number))
ascending()
"""
"""def descending():
    number=[4,3,2,5,7,4,2,1]
    print(sorted(number,reverse=True))
descending()"""
#🔹 Advanced (Logic & Real-life)
#Find the largest and smallest number in a list without using max() or min().
"""def largest():
    largest=[]
    number=[1,4,5,2,7,8,0,8,9]
    for num in number:
        largest.append(num)
    largest=max(largest)
    print(f"Largest: {largest}")
largest()

"""
#Given [3,5,7,9], calculate the sum and average.
"""def sum():
    sum=0
    number=[3,5,7,9]
    for num in number:
        sum +=num
    average= sum/ len(number)
    print(f"Sum: {sum}")
    print(f"Average: {average}")

sum()"""
#Join a list of words ["I", "love", "Python"] into a single sentence.
"""def join():
    words=["I", "love", "Python"]
    sentences=''
    for word in words:
        sentences += word + " "
    print(sentences.strip())
join()"""
#Create a shopping cart list. Ask user input for items until they type "done", then print the cart.
"""def item():
    while True:
        list=[]
        items=input("Enter Items or( d to done): ").strip().title()
        if items.lower() =='d':
          break
        list.append(items)
    print("\nShopping Cart")
    for item in list:
       
      print(item)

item()"""
#Rotate a list: [1,2,3,4,5] → [5,1,2,3,4].
"""def rotate():
    number=[1,2,3,4,5]
    rotate=number[-1:] + number[:-1]
    print(rotate)
rotate()"""
#🔹 Pro Level (Data Structures & Real-life Problems)
#Store student marks in a list and find the highest scorer.
"""def marks():
    highest=[]
    marks=[25,50,36,89,99,45,67]
    for mark in marks:
        highest.append(mark)
    highest=max(highest)
    print(f"Highest: {highest}")
marks()"""





       
          



