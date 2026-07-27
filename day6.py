# Decision making

# COMPARISON OPERATORS
# ==  Equal
# != Not equal
# > Greater than
# < Less than
# >= Greater than or equal
# <= Less than or equal

# IF STATEMENT
#if condition:
    # do something if condition is True
#else:
    # do something else if condition is False

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

    # if-elif-else statement
age = 10
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

    # LOGICAL OPERATORS
# and, or, not

age = 12
is_available = True

if age >= 18 and age < 65 and is_available:
    print("You are an adult and available.")
else:
    print("You are either not an adult or not available.")
    if not is_available:
        print("You are not available.")
    else:
        print("You are not an adult.")