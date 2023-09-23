from random import randint

class Incuficcientfunds(Exeption):
    pass
class InvalidTransaction(Expetion):
    pass
class Accountnotfound(Exeption):
    pass
class Bank_Account:
    def __init__(self):
        self.name = []
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def create_account(self):
        name = input("enter your name: ")
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        self.name += name
        print("\n new account created:",name ,"\n with balance of: " ,amount)

    def deposit(self):
        amount1 = float(input("enter amount to be deposited: "))
        self.balance += amount1
        print("\n deposited to account: ", amount1, "\nthe balance now is: ", self.balance)

    def withdraw(self):
        amount1 = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount1:
            self.balance -= amount1
            print("\n You Withdrew:", amount1,"\n the balance now is",self.balance)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

s = Bank_Account()

s.create_account()
s.deposit()
s.withdraw()