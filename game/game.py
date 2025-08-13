import random
import sys
import time
import csv
import os
import webbrowser   # To open CSV file

score_file = 'scores.csv'

def save_score(name, level, attempt, time_taken):
    file_exists = os.path.isfile(score_file)
    with open(score_file, 'a', newline='') as file:
        writer = csv.writer(file)
        # Fix typo: writerrow -> writerow
        if not file_exists:
            writer.writerow(['Name', 'Level', 'Attempts', 'Time(sec)'])
        writer.writerow([name, level, attempt, round(time_taken, 2)])

def show_score():
    if not os.path.exists(score_file):
        print("No Past Score Yet.")
        return
    print("\n--- Past Scores ---")
    with open(score_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# ----------- MAIN GAME -------------
if len(sys.argv) < 2:
    print("Kindly Enter your name Like:\npython day3.py musfira")
else:
    name = sys.argv[1]
    print(f"Welcome {name} to number guessing game!")

    # Show previous scores when game starts
    show_score()

    while True:
        level = input("\nSelect Level (easy/hard): ").strip().lower()
        if level == 'easy':
            max_val = 20
        elif level == 'hard':
            max_val = 100
        else:
            print("Invalid Level, Defaulting to easy.")
            max_val = 20

        secret = random.randint(1, max_val)
        start_time = time.time()
        attempt = 0

        while attempt < 7:
            try:
                guess = int(input("Guess: ").strip())
                attempt += 1
                if guess < secret:
                    print(f"Too Low, Try again\nAttempt Left: {7 - attempt}")
                elif guess > secret:
                    print(f"Too High, Try again\nAttempt Left: {7 - attempt}")
                else:
                    print(f"\nCongratulation {name}! You guessed the correct number {secret} after {attempt} attempts.")
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    minutes, second = divmod(elapsed_time, 60)
                    print(f"You Took {int(minutes)} minute(s) {round(second,2)} second(s)")

                    # Save score to CSV
                    save_score(name, level, attempt, elapsed_time)
                    break

            except ValueError:
                print("Invalid Input, allow only integers.")

        if guess != secret:
            print(f"\nGame over! You used all {attempt} attempts.\nSecret number was {secret}")

        # Ask replay
        play_again = input("\nDo You want to play again(yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Exiting-------")

            # Open CSV file automatically at exit
            if os.path.exists(score_file):
                webbrowser.open(score_file)   # Opens in Excel/Default viewer
            break
