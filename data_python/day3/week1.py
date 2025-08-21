#CS50P Week 1
#Deep Thought
"""def thoughts():
    answer=input("answer to the Great Question of Life, the Universe, and Everything: ").strip()
    if answer in['42','forty_two','forty two']:
        print(f"Your answer {answer} is correct.")
    else:
        print(f"Your answer {answer} is not correct.")
thoughts()"""
#Home Federal Savings Bank
"""def bank():
    greet=input("Enter Greet: ").strip()
    if greet.startswith('hello'):
        print("$0")
    elif greet.startswith('h'):
        print("$20")
    else:
        print("$100")
bank()"""
#File Extensions
"""def extension():
    file=input("Enter Filename: ").strip()
    if file.endswith('gif'):
        print('image/gif')
    elif file.endswith('jpg,jpeg') :
        print('image/jpeg')
    elif file.endswith('png'):
        print('image/png')
    elif file.endswith('pdf'):
        print('application/pdf')
    elif file.endswith('text'):
        print('text/plain')
    elif file.endswith('zip'):
        print('application/zip')
    else:
        print("application/octet-stream.")
extension()
"""
#Math Interpreter
def interpreter():
    expression=input("Enter Expression Like(1 + 3): ").strip()
    x,op,y=expression.split()
    x=float(x)
    y=float(y)
    if op == '+':
        result= x + y
    elif op == '-':
        result= x - y
    elif op == '*':
        result= x * y
    elif op == '/':
        result= x / y
    print(f"{result: 1f}")
interpreter()


    
