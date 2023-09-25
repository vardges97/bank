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

    def welcome_screen(self):
        while True:
            print("to create an account press 1\n"
              "to deposit to an account press 2\n"
              "to withdraw from n account press 3\n"
              "to transfer between accounts press 4\n"
              "to check the balance press 5\n"
              "to exit press 0\n")

            welcome_screen_select = str(input())
            if welcome_screen_select == "1":
                self.create_account()
            if welcome_screen_select == "2":
                self.deposit()
            if welcome_screen_select == "3":
                self.withdraw()
            if welcome_screen_select == "4":
                self.transfer()
            if welcome_screen_select == "5":
                self.display()
            if welcome_screen_select == "0":
                print("Goodbye")
                break

    def create_account(self):
        name = input("enter your name: ")
        balance = float(input("Enter amount to be deposited: "))
        self.accounts.update({name:balance})
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
        print("transfer from:",user1," for: ",amount,"to :",user2)
        print("transfer completed successfully.")

    def display(self):
        print("\n Net Available Balance= ", self.accounts)

x= Bank_Account()
print(x.welcome_screen())