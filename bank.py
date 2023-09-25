from random import randint

class Incuficcientfunds(Exception):
    pass
class InvalidTransaction(Exception):
    pass
class Accountnotfound(Exception):
    pass
class Bank_Account:
    def __init__(self):
        self.accounts = {}
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def create_account(self):
        name = input("enter your name: ")
        balance = float(input("Enter amount to be deposited: "))
        #self.balance += amount
        #self.name += name
        self.accounts.update({name.balance})
        print("\n new account created:",name ,"\n with balance of: " ,balance)

    def deposit(self):
        user = input("input the name of the account to which you wish to deposit: ")
        if user not in self.accounts:
            print("no user by that name found")
            return

        amount = float(input("enter the desired deposit amount: "))
        if amount< 0:
            raise InvalidTransaction("invalid transaction")
        self.accounts[user]+= amount
        print("\n deposited to account: ", amount, "\nthe balance now is: ", self.accounts)

    def withdraw(self):
        user = input("input the name of the account from which you wish to withdraw: ")
        if user not in self.accounts:
            print("user not found")
            return
        amount = float(input("Enter amount to be withdrawn: "))
        if amount > self.accounts[user]:
            raise Incuficcientfunds("invalid transaction!")
        if self.accounts[user] >= amount:
            self.accounts[user]-= amount
            print("\n you withdrew: ", amount,"\n the balance now is: ",self.accounts)
        else:
            print("insufficient funds")

    def transfer(self):
        user1 = input('enter the name of the account from which you want to transfer the funds: ')
        user2 = input("enter the name of the account you want to transfer the funds: ")
        if user1 not in self.accounts:
            raise Accountnotfound("user does not exist")
        if user2 not in self.accounts:
            raise Accountnotfound("user not found")

        amount = float(input(" what amount you wish to transfer: "))

        if self.accounts[user1] - amount < 0:
            raise Incuficcientfunds("you dont have enough funds to complete the transfer.")
        self.accounts[user1] -= amount
        self.accounts[user2] += amount
        print("transfer completed successfully.")

    def display(self):
        print("\n Net Available Balance= ", self.accounts)

s = Bank_Account()

s.create_account()
s.deposit()
s.withdraw()