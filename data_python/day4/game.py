#Number Guessing Game
import random
import sys
if len(sys.argv) !=2:
    print("Kindly enter your filename and name like: \ngame.py musfira")
else:
    name=sys.argv[1]
    print(f"Welcome {name}! Number Guessing Game")
    while True:
        level=input("Select Level(easy/high): ").strip().lower()
        if level=='easy':
            max_level=20
        elif level=='high':
            max_level=100
        else:
            print("Invalid Level,defaulting to easy.")
            max_level=20
        secret=random.randint(1,max_level)
        attempt=0
        while attempt < 7:
            try:
                guess=int(input("Guess: ").strip())
                attempt +=1
                if guess < secret:
                    print(f"Too Low,Try Again\nAttempt Left: {7 - attempt}")
                elif guess > secret:
                    print(f"Too High,Try Again\nAttempt Left: {7 - attempt}")
                else:
                    print(f"Congratulation {name}! You Have Guessed The  Correct Number {secret} After {attempt} attempts.")
                    
            except ValueError:
                print("Invalid Input, allow only integers")
        if guess != secret:
            print(f"You have used all your {attempt} attempts.\nThe Secret number is {secret} ")
            play_again=input("Play Again(yes/no): ").strip().lower()
            if play_again!='yes':
                break







