#import library used for choice generate number and shuffle
"""import random
coin=random.choice(["head","tail"])
print(coin)"""
"""from random import choice
coin =choice(["Heads","Tails"])
print(coin)"""
"""import random
number=random.randint(1,10)
print(number)"""
#shuffle
"""import random
cards=["jacky","mory","nooory"]
random.shuffle(cards)
for card in cards:
  print(card)"""
#number guessing game
"""import random
def number_guessing_game():
  number=random.randint(1,10)
  guess=None
  attempt=0
  print("Welcome to the number guess game!")
  print("Select the number between (1,10).")
  while True:
    try:
      #take input from the user
      guess=int(input("Guess: "))
      attempt+=1
      #use conditional
      if guess>number:
        print(f"{guess} is Too high,Try again!")
      elif guess<number:
        print(f"{guess} is Too low,Try again!")
      else:
        print(f"Congratulation: you won {guess} number after {attempt} attempts.")
        print("Thank you soo much!")
        break
    except ValueError:
      print("kindly input integers only.")
number_guessing_game()"""
#🔹 Random Choice Questions 
# 1️⃣ Random Fruit Picker 🍎🍌🥭
"""Create a program that randomly selects a fruit from a list: ["Apple", "Banana", "Mango", "Orange", "Grapes"] and prints the selected fruit."""
import random
def fruit_picker():
  fruits=(["Apple", "Banana", "Mango", "Orange", "Grapes"])
  selected=random.choice(fruits)
  print("Available Fruits:", ",".join(fruits))
  guess=input("which fruit is selected: ").strip().capitalize()
  if guess==selected:
    print(f"correct: it was {selected}")
  else:
    print(f"nope! it was {selected}")
fruit_picker()
 











