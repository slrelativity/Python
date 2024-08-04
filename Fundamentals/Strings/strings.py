#string interpolation / a way to inject variables into strings (alpha/numeric)

first_name = "Sean"

last_name = "lawson"

print(f"Hello my name is {first_name } {last_name.capitalize()}") 

#prints Hello my name is Sean Lawson

# or

print("Hello my name is {} {}"  .format(first_name, last_name))
#prints Hello my name is Sean lawson


print("this is a sample string")
#this is a sample string


#concated strings
name = "Zen"
print("My name is " + name)
#prints My name is Zen



#print("Hello " + 42)			# output: TypeError due to interger
print("Hello " + str(42))		# output: Hello 42


total = 35
user_val = "26"
#total = total + user_val		# output: TypeError due to interger
total = total + int(user_val)		# total will be 61

print(total)


#f strings (can use variables)
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#string.format / goes in order of the format
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.


# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5
greeting = ("Hello my name is {} {}.".format(first_name, last_name))
print(greeting) 
# Desired output: Hello my name is Alana Da Silva
print("I am {} years old".format(age)) 
# Desired output: I am 36 years old
print(f"I work as a {profession}.")
# Desired output: I work as a Software Developer.
exp_string = "I have worked in the field for {} years."
print(exp_string.format(age))
# Desired output: I have worked in the field for 5 years.
print(f"I started in the field when I was {age - years_experience} years old.".format(age, years_experience))

#or

print(f"I started in the field when I was", int(age - years_experience),  "years old.")
# Desired output: I started in the field when I was 31 years old.


x = "hello world"
print(x.title())
# output:
"Hello World"




