class User:
    #Declaring a class
    def __init__(self, first_name, last_name, email, age):
        #assigning
        self.first_name = first_name #class attribute
        self.last_name = last_name #class attribute
        self.email = email #class attribute
        self.age = age #class attribute
        self.is_rewards_member = False #Status is set to False by default
        self.gold_card_points = 0 #Status is set to 0 by default

 
    def display_info(self):
        print(f"{self.first_name}") 
        print(f"{self.last_name}")
        print(f"{self.email}")
        print(f"{self.age}")
        print(f"{self.is_rewards_member}")
        print(f"{self.gold_card_points}")
    
    
    def enroll(self):
        if self.is_rewards_member: #This is checking to see if the user is a rewards member
            print("You are already a rewards member!") #Printing out that they are already a rewards member status
            return False #Returning if condition
        else:
            self.is_rewards_member = True #Checking condition
            print("You are a rewards member!") #Printing out they're are a rewards
            self.gold_card_points = 200 #Setting gold card points value
            return True #Returning else condition
        
    def spend_points(self, amount):
            if self.gold_card_points >= amount: #This is checking to see if you have enough points to spend if 200 is greater than or equal to the value
                print("You have enough to spend!") #Printing user has enough gold points to spend
                self.gold_card_points -= amount #This is the amount of points you have to spend
            else:
                print("You don't have enough...") #Printing that user does not have enough points
chris_user = User("Chris", "Allen", "callen@msn.com", 29,) #User 1 attributes
chris_user.display_info() #Displaying user info

chris_user.enroll() #Enrolling user
print(f"{chris_user.first_name} is now enrolled") #Printing Chris is now enrolled

chris_user.display_info() #Displaying user info
chris_user.spend_points(50) #Sharing points spent
print(f"{chris_user.first_name} just spent 50 gold card points") #Printing out gold points spent
chris_user.display_info() #Displaying user info

print("======================================================")

keith_user = User("Keith", "Ball", "kball@msn.com", 39,)
keith_user.display_info() #Displaying user info

keith_user.enroll() #Enrolling user
print(f"{keith_user.first_name} is now enrolled") #Printing Chris is now enrolled

keith_user.display_info() #Displaying user info
keith_user.spend_points(80) #Sharing points spent
print(f"{keith_user.first_name} just spent 80 gold card points") #Printing out gold points spent
keith_user.display_info() #Displaying user info
