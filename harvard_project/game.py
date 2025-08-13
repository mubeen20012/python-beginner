#Day 1: Core Python Revision (Basics, Conditionals, Loops)
#Mini Project: Number Guessing Game

import sys
import random
import time
import os
import csv
import webbrowser
score_file='score.csv'
def save_score(name,level,attempt,time_taken):
    file_exists=os.path.isfile(score_file)
    with open(score_file,'a',newline='') as file:
        writer=csv.writer(file)
        if not file_exists:
            writer.writerow(['Name','Level','Attempts','time(sec)'])
        writer.writerow([name,level,attempt,round(time_taken,2)])
def show_score():
    if not os.path.exists(score_file):
        print("No Previous Score Yet.")
        return
    print("---Past Score---")
    with open(score_file,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)

if len(sys.argv) !=2:
    print("Kindly enter your name like:\npython filename name.")
else:
    name=sys.argv[1]
    print(f"Welcome {name}! Number Guessing Game")
    show_score()
    while True:
        level=input("Select Level(easy/hard): ").strip().lower()
        if level=='easy':
            max_range=20
        elif level=='hard':
            max_range=100
        else:
            print("Invalid Level,Defaulting to easy.")
            max_range=20
        secret=random.randint(1,max_range)
        start_time=time.time()
        attempt=0
        while attempt < 7:
            try:
                guess=int(input("Guess: ").strip())
                attempt +=1
                if guess < secret:
                    print(f"Too Low.Try Again\n (Attempt Left: {7 - attempt})")
                elif guess > secret:
                    print(f"Too High.Try Again\n (Attempt Left: {7 - attempt})")
                else:
                    print(f"Congratulation {name}! You Guess the correct number {secret} after {attempt} attempts.")
                    end_time=time.time()
                    elapsed_time=end_time - start_time
                    minutes,second=divmod(elapsed_time,60)
                    print(f"You took {int(minutes)} minute(s) and {round(second,2)} second(s).")
                    save_score(name,level,attempt,elapsed_time)
                    break
            except ValueError:
                print("Invalid Input,allow only integers.")
        if guess != secret:
            print(f"Game Over! The Secret number was {secret}.")  
        play_again=input("Do you want to play again(yes/no): ") .strip().lower() 
        if play_again!= 'yes':
            print("Exiting----")
            if os.path.exists(score_file):
                webbrowser.open(score_file)
            break






