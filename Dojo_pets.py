    #implement __init__( first_name , last_name , treats , pet_food , pet_name, pet_type, pet_tricks)
class Ninja:
    def __init__(self, first, last, treats, pet_food, pet_name, pet_type, pet_tricks): 
        self.first_name = first
        self.last_name = last
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name , pet_type , pet_tricks)
    
    # implement the following methods:

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self


    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat() 
        print(f"{self.first_name} likes to feed {self.pet.name}{self.pet_food}")


    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} doesn't like bathing {self.pet.name}")

class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(name , type , tricks ):
        self.name = name
        pet_type = type
        pet_tricks = tricks
        pet_energy = 25
        pet_health = 25


    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy +=25
        print(f"{name} is sleeping and energy increases to {self.energy}")
     

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy +=5
        self.health += 10
        print(f"{name} is eating and energy increases {self.energy} to {self.health}")



    # play() - increases the pet's health by 5
    def play():
        pet_energy +=5
        pet_energy +=25
        print(f"{name} is playing and energy increases {self.health}")


    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{name} barks a lot")


user = Pet("Bosco", "fetch", "") #User 1 attributes