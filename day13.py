#FUNCTIONS_secret to reusable code
# A FUNCTION IS A REUSABLE BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK. IT CAN TAKE INPUTS, PROCESS THEM, AND RETURN OUTPUTS. FUNCTIONS HELP ORGANIZE CODE, MAKE IT MORE READABLE, AND ALLOW FOR CODE REUSE.
# whatsapp
# press send
# send_message()

#ATM
# withdraw
# withdraw_money()

def welcome():
    print("Welcome to the program!")

welcome()
welcome()

#FUNCTIONS WITH PARAMETERS
def greet(name):
    print(f"Hello, {name}!")
    

greet("Alice")
greet("Bob")
greet("Charlie")

#MULTIPLE PARAMETERS
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

    #calling the function 
introduce("Alice", 25)
introduce("Bob", 30)
introduce("Charlie", 35)

#return values from functions
def add_numbers(a, b):
    print(a + b)

    add_numbers(5, 3)

    answer = add_numbers(5, 3)
    print(answer)  # This will print None because the function does not return a value

# To make the function return a value, use the return statement
def add_numbers(a, b):
    return a + b

answer = add_numbers(5, 3)
print(answer)  # This will print 8

#PRINT                           VS           RETURN
# display info on the screen                   sends information back to the caller
# cannot be reused                             can be reused in other parts of the program
# used for output purposes only                used for further calculations or processing
# mainly for the user to see the result        mainly for the program to use the result

#I would love to to visit (city) with friend
def visit_city(city, friend):
    return f"I would love to visit {city} with {friend}."

message = visit_city("Paris", "Alice")
print(message)
