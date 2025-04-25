#🔐 1. Encapsulation Exercise
#🎯 Goal: Use private variables and public methods to interact
#📝 Practice Exercise:
class BankAccount:
    def __init__(self,balance=0,account_number=None):
        self.__balance=balance
        self.__account_number=account_number
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount.")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Imsufficient amount to withdraw\nKindly recharge your account")
        else:
            self.__balance-=amount
            print(f"Withdrawn: {amount}")
            print(f"Balance: {self.__balance}")
    def get_amount(self):
        if self.__balance==0:
            print("No balance\nKindly Recharge Your Accoount.")
        else:
            print("--Show Balance--")
            print(f"Balance: {self.__balance}")
    def get_account_number(self):
        return self.__account_number
def main():
        account=BankAccount(account_number=1234567890)
        print("--Show Menu--")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Check Balance")
        print("4.Exit")
        while True:
            try:
                choice=int(input("choice: "))
                if choice==1:
                    amount=int(input("Amount to Deposit: ").strip())
                    account.deposit(amount)
                elif choice==2:
                    amount=int(input("Amount to Withdraw: ").strip())
                    account.withdraw(amount)
                elif choice==3:
                    account.get_amount()
                elif choice==4:
                    print("Thank You.")
                    break
                else:
                    print("Invalid Choice.")
            except ValueError:
                print("Invalid Input.")
if __name__=="__main__":
        main()

    
        



        pass