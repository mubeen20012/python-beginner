#💡 5 Extra Logic-Building Problems (Week 1 Style)
#Even or Odd
"""def main():
    try:
      number=int(input("Number: ").strip())
      print(f"Your number is: {even(number)}")
    except ValueError:
       print("Invalid Input,allow only integers.")
def even(number):
   if number %2==0:
      print("Even")
      return number
   else:
        print("Odd")
  
main()
"""
"""def even():
    try:
        number=int(input("Number: ").strip())
        if number %2==0:
            print(f"Number {number} is even.")
        else:
            print(f"Number {number} is odd.")
    except ValueError:
        print("Invalid Input, allow only integers.")
even()"""



#Password Strength Checker
"""def password():
    password=int(input("Enter Password: ").strip())
    if password >=8:
        print("Invalid Password.Password must be 8.")
    else:
        print(f"Password {password} is Valid.")
password()"""
#FizzBuzz
"""def fizz():
    for num in range(1,21):
        if num %3==0 and num %5==0:
            print("FizzBuzz")
        elif num %3==0:
            print("Fizz")
        elif num %5==0:
            print("Buzz")
        else:
            print(num)
fizz()"""
#Temperature Converter
def converter():
   try:
      celcius=int(input("Enter Temperature: ").strip())
      F=(celcius * 9/5) + 32
      print(f"Temperature in Fehrenheit: {F}")
   except ValueError:
      print("Invalid Input, allow only integer.")
converter()
