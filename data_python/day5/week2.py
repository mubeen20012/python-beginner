#Harvard CS50P Week 2 Problem Set
#camelCase
"""def main():
    name=input("Enter CamelCase: ").strip()
    print(f"Snake_case: {snake_case(name)}")
def snake_case(name):
    result=''
    for char in name:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result +=char
    return result
    
main()"""
#Coke Machine
"""def machine():
    amount =50
    while amount >0:
        try:
            coin=int(input("Insert Coin: ").strip())
            if coin in (5,10,25):
                print(f" your coin {coin} is Valid.")
                amount -= coin
                print(f"Remaining Amount: {amount}")
            else:
                print(f"Your Coin {coin} is not Valid.")
            if amount >0:
                print(f"Amount Due: {amount}")


        except ValueError:
            print("Invalid, allow only integers.")
    print(f"Owed: {abs(amount)}")
machine()"""
#Just setting up my twttr
"""def twitter():
    twitter=''
    tweet=input("Enter Tweet: ").strip()
    vowels='AEIOUaeiou'
    for char in tweet:
        if char not in vowels:
            twitter += char
    print(f"Twitter: {twitter}")
twitter()"""
#Vanity Plates
"""def vanity():
    plate=input("Enter Plate number: ").strip()
    if len(plate) <2 or len(plate)>6:
        print("Invalid")
        return
    if not plate[:2].isalpha():
        print("Invalid")
        return
    if not plate.isalnum():
        print("Invalid")
        return
    for i,char in enumerate(plate):
        if char.isdigit():
            if char ==0:
                print("Invalid")
                print("First Digit cannot be 0.")
                return
        if not plate[i:].isdigit():
                print("Invalid")
                return
        break


vanity()"""
#Nutrition Facts
def fruits():
 fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew": 50,
    "kiwi": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70
}
 while True:
  name=input("Enter Fruit Name(or q to quit): ").strip()
  if name== 'q':
   print("Exiting-----")
   break
  if not name:
   print("Kindly Enter Fruit Name To check the Calories.")
   continue
  for fruit in name:
   print(f"Calories: {fruit(fruits)}")
fruits()





