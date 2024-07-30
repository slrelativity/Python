num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #data type boolean is true
string = 'Hello World' #setting string equal to Hello World
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #composite list 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionaries
fruit = ('blueberry', 'strawberry', 'banana') #tuples access value
print(type(fruit)) #output class tuple 
print(pizza_toppings[1]) #print sausage
pizza_toppings.append('Mushrooms')  #will add Mushrooms to the end of  ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
print(person['name'])  #will print the name John
person['name'] = 'George' #updates the name to George
person['eye_color'] = 'blue' #updates or adds the eye color
print(fruit[2]) #will print out fruit at access value 2

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #will print it's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)    #prints sequence of numbers from 0 to 4
for x in range(2,5):
    print(x)    #prints sequence of numbers from 2 to 4
for x in range(2,10,3):
    print(x)    #prints sequence of numbers from 2 to 9, but increment by 3
x = 0
while(x < 5):
    print(x)    #will loop though while x is less than 5 and increase by one as long as it's less than 5
    x += 1 

pizza_toppings.pop() #updates the name to 'name: George'
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)