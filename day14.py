# FUNCTION ARGUMENTS AND SCOPE
# We learn how to make our functions much smarter

def order_pizza(size, toppings):
    print(f"{size} pizza with {toppings}")

order_pizza("Large", "pepperoni and mushrooms")

#1 POSSITIONAL ARGUMENTS
# They depend on the order

def student(name, age):
    print(name, age)

student("Alice", 20)  # Correct order

#2 KEYWORD ARGUMENTS
# They are independent of the order
# Let's us specify which value goes to which parameter
student(age=20, name="Alice")  # Correct order

#3 DEFAULT ARGUMENTS
# They are used when we want to provide a default value for a parameter

def pay(amount, currency="KSH"):
    print(f"Paying {amount} {currency}")

pay(1000)  # Uses default currency
pay(1000, "USD")  # Overrides default currency

#SCOPE
# It refers to the region of the code where a variable is accessible

#Local Scope
def test():
    x=10
    print(x)  # x is accessible here

test()

#Global Scope
school = "ABC School"  # Global variable

def print_school():
    print(school)  # school is accessible here

print_school()

def calculated_area(length, width):
    area = length * width  # Local variable
    return area

print(calculated_area(5, 10))  # Calls the function and prints the area