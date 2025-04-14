# 📝 Mini Project: Student Record App:
#create a student class
class Student:
  def __init__(self,name,roll_no,department,cgpa):
    self.name=name
    self.roll_no=roll_no
    self.department=department
    self.cgpa=cgpa
  def __str__(self):
    return(f"Name: {self.name}\n"
    f"Roll_No: {self.roll_no}\n"
    f"Department: {self.department}\n"
    f"CGPA: {self.cgpa}")
students=[]
def add_student():
  name=input("Enter Name: ").title().strip()
  roll_no=input("Enter Roll_No: ").title().strip()
  department=input("Enter Department: ").title().strip()
  cgpa=float(input("Enter CGPa: ").strip())
  student=Student(name,roll_no,department,cgpa)
  students.append(student)
  print("Student added Successfully.")
def view_student():
    if not students:
        print("No student found.")
    else:
       for student in students:
        print(student)
        print('-'*20)
def main():
    print("\nStudent Record App!")
    print("a.Add Student")
    print("2.View Student")
    print("3.Exiting")
    while True:
      try:
          choice=int(input("Enter your choice: "))
          if choice==1:
             add_student()
          elif choice==2:
             view_student()
          elif choice==3:
             print("Exiting---")
             break
          else:
             print("Invalid choice.")
      except ValueError:
            print("Invalid Input.")
if __name__=="__main__":
    main()
      
    

    

           

