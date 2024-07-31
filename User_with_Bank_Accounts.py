class User:
    def __init__(self, first, last, email):
        self.first_name = first
        self.last_name = last
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    

    # other methods
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    

    def make_deposit(self, amount):
        # your code here
        self.account.deposit(amount)
        return self
    

    def make_withdrawl(self, amount):
        # your code here
        self.account.withdraw(amount)
        return self


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)        
        self.int_rate = int_rate
        self.balance = balance

        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposit. Balance is {self.balance}")

    def withdraw(self, amount):
        # your code here
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Balance is {self.balance}")
        else:
            print("Insufficent funds")

    def display_account_info(self):
        # your code here
        print(f"{self.int_rate}")
        print(f"{self.balance}")

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
        
chris_user = User("Chris", "Allen", "callen@msn.com") #User 1 attributes
chris_user.display_user_balance()#Displaying account info

chris_user.make_deposit(60)
chris_user.account.yield_interest()
chris_user.make_deposit(60)
chris_user.account.yield_interest()
chris_user.make_deposit(60)
chris_user.account.yield_interest()
chris_user.make_withdrawl(130)
chris_user.display_user_balance()#Displaying account info


print("===================================================")

angela_user = User("Angela", "Sade", "asade@msn.com") #User 1 attributes
angela_user.display_user_balance() #Displaying account info

angela_user.make_deposit(60)
angela_user.account.yield_interest()
angela_user.make_deposit(450)
angela_user.account.yield_interest()
angela_user.make_withdrawl(200)
angela_user.account.yield_interest()
angela_user.make_withdrawl(40)
angela_user.account.yield_interest()
angela_user.make_withdrawl(100)
angela_user.account.yield_interest()
angela_user.make_withdrawl(260)