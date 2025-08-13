import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) !=2:
        print("Kindly enter filename")
    else:
        filename=sys.argv[1]
        print(pizza_menu(filename))
def pizza_menu(filename):
  try:
    with open(filename,'r') as file:
        reader=csv.DictReader(file)
        table=list(reader)
        print(tabulate(table,headers='firstrow',tablefmt='grid'))
  except FileNotFoundError:
     print("File not found.")
if __name__=='__main__':
   main()
