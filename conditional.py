"""#✅ Today’s (Day 1) 1‑Hour Revision Plan
#Practice Problems (5)
#1. Swap two variables without a third.
name=input("Enter name: ").strip().title()
age=int(input("age: "))
name,age=age,name
print(f"name now: {name} ")
print(f"age now: {age}")
a=5
b=7
a,b=b,a
print(a)
print(b)"""
#2. Average calculator: read three numbers, print their greater.
"""a=6
b=7
c=8
if a>b or a>c:
    print(f"{a} is graeter than {b},{c}")
elif b>a or b>c:
    print(f"{b} is graeter than {a},{c}")
else:
    print(f"{c} is graeter than {a},{b}")
#average number:
a=int(input("Number: "))
b=int(input("Number: "))
c=int(input("Number: "))
average=(a+b+c)/3
print(f"The average of {a},{b},{c} is: {average}")"""
#🧠 Challenge: Build a “Student Score App” that takes name and score, prints if student passed or failed (score ≥ 50).
name=input("Name: ").strip().title()
score=int(input("Score: ").strip())
if score>=90 and score<=100:
    print(f"{name} Score is: A+")
    print("Excellent")
elif score>=80 and  score<=90:
    print(f"{name} Score is: A+")
elif score>=70 and  score<=80:
    print(f"{name} Score is: B")
elif score>=60 and  score<=70:
    print(f"{name} Score is: C")
elif score>=50 and  score<=60:
    print(f"{name} Score is: D")
else:
    print("Fail")
    print("Try next time")



