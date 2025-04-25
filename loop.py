"""#Sum of Even Numbers
def even():
    sum=0
    for i in range(1,101):
        if i%2==0:
            sum+=i
    print(f"Sum of all even number is: {sum}")
even()
#Reverse a String
def reverse():
    name=input("Name: ").title().strip()
    for i in range(len(name)-1,-1,-1):
        print(name[i],end="")
reverse()
"""
#Multiplication Table
"""def Table():
    num=int(input("Enter a Table: "))
    print(f"Table of {num} is: ")
    for i in range(1,11):
        print(f"{num} * {i}={num*i}")
Table()"""
#Count Vowels
"""def count():
    name=input("Name: ").lower().strip()
    vowels="aeiou"
    count=0
    for i in name:
        if i in vowels.lower():
            count+=1
    print(f"Number of vowels in {name} is:  {count}")
count()"""
#Factorial Calculator
"""def factorial():
    num=int(input("Enter a number: "))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"Factorial of number {num} is: {fact}")
factorial()"""
#Print Pattern
"""def pattern():
    number=int(input("Enter a number: "))
    for i in range(1,number+1):
        print("*"*i)
        number+=1
pattern()"""
#💼 Mini Project: Simple ATM Simulation
def ATM():
    balance=0
    print("Welcome to the ATM")
    print("\n--Menu--")
    print("1.Deposit")
    print("2.Check Balance")
    print("3.Withdraw ")
    print("4.Exit ")
    while True:
        try:
            choice=int(input("Choice: "))
            if choice==1:
                deposit=int(input("Enter amount to deposit: "))
                balance+=deposit
                print(f"Deposited: {deposit}")
                print(f"New Balance: {balance}")
            elif choice==2:
                print("\n--Balance--")
                if balance==0:
                    print("No balance")
                else:
                    print(f"Balance: {balance}")
            elif choice==3:
                withdraw=int(input("Enter amount to withdrawn: "))
                if withdraw<=balance:
                    balance-=withdraw
                    print(f"Withdrawn: {withdraw} ")
                    print(f"New balance: {balance}")
                else:
                    print("Insufficient balance")
            elif choice==4:
                print("Thank you for using ATM.")
                break
            else:
                print("Invalid choice,please try again.")
        except ValueError:
            print("Invalid input,please netre a number.")
ATM()

         





