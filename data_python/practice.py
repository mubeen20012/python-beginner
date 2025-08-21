"""#Read and write CSV
import os
import csv
score_file='score.csv'
#write csv
def save_score(name,level,attempt,score):
    file_exists=os.path.isfile(score_file)
    with open(score_file,'a',newline='') as file:
        writer=csv.DictWriter(file)
        if not file_exists:
            writer.writerow(['Name','Level','Attempt','Time'])
        else:
            writer.writerow(name,level,attempt,score)
def show_score():
    if not os.path.exists(score_file):
        print("No Past Score Yet.")
    else:
        with open(score_file,'r') as file:
            reader=csv.DictReader(score_file)
            for row in reader:
                print(row)
if os.path.exists(score_file)"""
#csv practice
import os
import csv
score_file='score.csv'
def save_score(name,level,attempt,time_taken):
    file_exists=os.path.isfile(score_file)
    with open(score_file,'a',newline='') as file:
        writer=csv.DictWriter(file)
        if not file_exists:
            writer.writerow(['Name','Level','Attempt','Time'])
        else:
            writer.writerow([name,level,attempt,time_taken])
def show_score():
    if not os.path.exists(score_file):
        print("No Past Score Yet.")
        with open(score_file,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                print(row)
    if  os.path.exists(score_file):
       


