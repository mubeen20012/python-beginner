#🕐 1-Hour Python Logic-Building Exercises
#Warm-up (10 minutes)
#Odd or Even Checker
"""def even():
    for number in range(5):
        try:
            number=int(input("Enter Number: ").strip())
            if number %2==0:
               print(f"Even Number {number}")
        except ValueError:
            print("Invalid Input,allow only integers.")
            
even()"""
#Reverse a Number
"""def number():
    try:
        number=int(input("Number: ").strip())
        reverse=0
        while number >0:

          digit=number%10
          reverse=reverse * 10 + digit
          number//=10
        print(f"Reverse: {reverse}")
    except ValueError:
       print("Invalid Input, allow only integers.")
number()"""
# sum
"""def sum():
    try:
        number=int(input("Number: ").strip())
        sum=0
        while number >0:
            digit=number%10
            sum=sum + digit
            number//=10
        print(f"Sum: {sum}")
    except ValueError:
       print("Invalid Input, allow only integers.")
sum()"""
#Lists & Loops (15 minutes)
"""def largest():
    list=[]
    for number in range(5):
        try:
            number=int(input("Number: ").strip())
            list.append(number)
        except ValueError:
            print("Invalid Input, allow only integers.")
    largest=list[0]
    for n in list:
        if n> largest:
            largest=n
    print(f"Largest: {largest}")
largest()"""
"""def largest():
    list=[]
    for number in range(5):
        try:
            number=int(input("Number: ").strip())
            list.append(number)
        except ValueError:
            print("Invalid Input, allow only integers.")
    largest=second=float('-inf')
    for n in list:
        if n>largest:
            second=largest
            largest=n
        elif n> second and n!=largest:
            second=n

    print(f" Second Largest Number: {second}")
largest()
"""
#Sum and Average
"""def sum():
    numbers=[]
    sum=0
    for number in range(5):
        try:
            number=int(input("Number: ").strip())
            numbers.append(number)
        except ValueError:
            print("Invalid Input, allow only integers.")
    for num in numbers:
        sum+=num
    print(f"Sum: {sum}")
    average=sum/len(numbers)
    print(f"Average: {average:.2f}")
sum()
"""
#Strings & Conditions (10 minutes)
def count():
    
    sentence=input("Sentence: ").strip()
    vowel='AEIOUaeiou'
    vowel_count=0
    consonent_count=0
    for char in sentence:
        if char in vowel:
            vowel_count+=1
    print(f"Vowels Count: {vowel_count}")
    for char in sentence:
        if char not in vowel:
            consonent_count +=1
    print(f"consent Count: {consonent_count}")


count()

