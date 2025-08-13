
import csv
filename='student.csv'
def save_score():
    with open(filename, 'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["name","age","grade"])
        writer.writerow(['musfira','22',90])
def show_score():
    with open(filename,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
save_score()
show_score()
##Exercise 2: Append New Record
import csv
import os
filename='student.csv'
def save_score():
    file_exists=os.path.isfile(filename)
    with open(filename,'a', newline='') as file:
        writer=csv.writer(file)
    if not file_exists:
        writer.writerow(['name','age','grade'])
    writer.writerow(['name','age','grade'])
def show_score():
    with open(filename,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
def filter_score():
    with open(filename,'r') as file:
        reader=csv.reader(file)
        header=next(reader)
        for row in reader:
            if int(row[2]) >80:
                print(row)
save_score()
show_score()
