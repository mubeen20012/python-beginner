"""def main():
    variable_name=input("Enter Camel case Variable: ").strip()
    print(f"Snake Case: {camel_to_snake(variable_name)}")
def camel_to_snake(name):
    snake_case=''
    for char in name:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case +=char
        if snake_case.startswith('_'):
            snake_case= snake_case[1:]
        return snake_case
main()
"""
"""def camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    # Remove leading underscore if it exists
    if snake_case.startswith("_"):
        snake_case = snake_case[1:]
    return snake_case

# Example usage:
variable_name = input("Enter camelCase variable: ").strip()
print("snake_case:", camel_to_snake(variable_name))"""
#Coke Machine
"""amount=50
while amount >0:
    try:
        coin=int(input("Insert Coin: ").strip())
        if coin in (5,10,25):
            print(f"Your Coin {coin} is Valid.")
            amount -= coin
            print(f"Remaining Amount: {amount} ")
        else:
            print(f"Your Coin {coin} is not Valid.")
    except ValueError:
        print("Invalid Input,allow only Integers.")
if amount <0:
    print(f"Change Owed: {abs(amount)}")
else:
    print(f"Change Owed: 0")"""
"""def twitter():
    tweet=input("Tweet: ")
    vowel='AEIOUaeiou'
    result=''
    for char in tweet:
        if char not  in vowel:
            result += char
    print(result)
twitter()"""
#Vanity Plate
def plate():
    name=input("Enter Name: ").strip()
    if len(name) <2 or len(name) >6:
        print("Invalid")
        return
    if not name.isalnum():
        print("Invalid, only letters and number allowed.")
        return
    if not name[0:2].isalpha():
        print("Invalid, first 2 character must be letters.")
        return
    for i,char in enumerate(name):
        if char.isdigit():
            if char =='0':
                print("Invalid:first character cannot be 0.")
                return
            if not name[i:].isdigit():
                print("Invalid: numbers must come at the end.")
                return
            break
plate()
"""def nutrition():
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
      fruit=input("Enter fruit name to check Calories:  ").strip().lower()
      if fruit=='q':
        print("Exiting----")
        break
                
      if not fruit:
              print("Kindly enter Fruit name.")
              continue
      if fruit in fruits:
              print(f"Calories: {fruits[fruit]}")
      else:
          print("Fruit not found in database")

nutrition()
"""





