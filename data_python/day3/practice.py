#CS50P Week 0
#1. Indoor Voice
#Write a program that gets input from the user and outputs it in lowercase.
"""def lower():
    user=input("Input: ").strip()
    output=user.lower()
    print(f"Your Output is: {output}")
lower()"""
#Playback Speed

#Take input text and output it with every space replaced by ....
"""def voice():
    text=input("Text: ").strip()
    voice=text.replace(" ","...")
    print(f"Output: {voice}")
voice()"""
#Making Faces

#Take a string and replace :) with 🙂 and :( with 🙁.
"""def main():
    user=input("Text: ").strip()
    print(f"Output: {emoji(user)}")
def emoji(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text
main()"""
#Einstein
#Prompt for m (mass in kg) and output E (energy) using E = m * c² where c = 300000000.
"""def main():
    mass=int(input("Enter Mass: ").strip())
    print(f"Energy in Joule: {energy(mass)}")
def energy(mass):
    C=300000000
    E=mass * C**2
    return E
main()"""
#Tip Calculator

"""Ask for meal cost and desired tip percentage,
then calculate and display the tip amount in dollars.
"""
def calculator():
    cost=float(input("Enter Cost: ").strip())
    percentage=float(input("How much would you like to give tip: ").replace(" ","%"))
    tip=(cost*percentage) / 100
    print(f"Your Tip is: ${tip:.2f}")
calculator()

