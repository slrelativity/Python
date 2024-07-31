class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, first, last, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.first_name = first #class attribute
        self.last_name = last #class attribute
        self.int_rate = int_rate
        self.balance = balance

        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. Balance is {self.balance}")
    def withdraw(self, amount):
        # your code here
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Balance is {self.balance}")
        else:
            print("Insufficent funds")
    def display_account_info(self):
        # your code here
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.int_rate}")
        print(f"{self.balance}")

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
        #your code here
        #if self.balance > 0:
        #self.balance * self.int_rate
        #self.int_rate += interest

chris_user = BankAccount("Chris", "Allen", .02, 400) #User 1 attributes
chris_user.display_account_info()#Displaying account info

chris_user.deposit(60)
chris_user.yield_interest()
chris_user.deposit(60)
chris_user.yield_interest()
chris_user.deposit(60)
chris_user.yield_interest()
chris_user.withdraw(130)

angela_user = BankAccount("Angela", "Sade", .02, 450) #User 1 attributes
angela_user.display_account_info() #Displaying account info

angela_user.deposit(60)
angela_user.yield_interest()
angela_user.deposit(45)
angela_user.yield_interest()
angela_user.withdraw(200)
angela_user.yield_interest()
angela_user.withdraw(40)
angela_user.yield_interest()
angela_user.withdraw(100)
angela_user.yield_interest()
angela_user.withdraw(260)