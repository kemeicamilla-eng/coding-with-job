#INPUT , Output, and Type Conversion

#OUTPUT
print("Hello, World!")
print("Welcome to 90 Days of Coding!")

#user input
name = input("Enter your name: ")
print("Hello,", name, "! Welcome to 90 Days of Coding!")

#F STRINGS
# easier to read
#no need to convert data types manually
#you can include operators

age = input("When were you born? ")
print(f"You are {2026 - int(age)} years old!")

height = input("What is your height in meters? ")
print(f"Your height is {float(height)} meters.")

#ERRORS
age = input("When were you born? ")
print(f"You are {2026 - int(age)} years old!")

# TYPE CONVERSION
# This is the process of converting one data type to another. For example, converting a string to an integer or a float.
# In Python, we can use the int(), float(), and str() functions to convert data types.

age = 20
print(float(age))  # Convert integer to float

# strings and indexing

county = "Nairobi"
print(county[0])  # Print the first character of the string
print(county[-1])  # Print the last character of the string
print(county[1:4])  # Print characters from index 1 to 3

name = "Camilla"
print(name.upper())  # Convert string to uppercase
print(name.lower())  # Convert string to lowercase
print(name.replace("C", "K"))  # Replace character in string
print(name.strip())  # Remove whitespace from the beginning and end of the string
