#LOOPS
# repeats something over and over again

print("Today is Thursday.")
# we print the above statement 5 times 

#TYPES OF LOOPS
# 1. for loop
# 2. while loop

#WHILE LOOP
i = 0
while i < 5:
    print("Today is Thursday.")
    i += 2

#FOR LOOP
for i in range(5):
    print("Today is Thursday.")


#range() function generates a sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
#range(5) generates numbers from 0 to 4 (5 numbers in total).
for i in range(5):
    print(i)

for i in range(0,12,2): # start, stop, step
    print(i)

for i in range(1,6): 
    print(i)

    #looping through strings
    for char in "Hello, World!":
        print(char)

#BREAK STATEMENT
# The break statement is used to exit a loop prematurely when a certain condition is met.
for i in range(1,11):
    if i == 6:
        break
    print(i)

#CONTINUE STATEMENT
# The continue statement is used to skip the current iteration of a loop and move on to the next iteration.
for i in range(1,11):
    if i == 6:
        continue
    print(i)

#PASSWORD CHECKER
password = "securepassword"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Password correct!")
        break
    else:
        print("Incorrect password.")
        attempts += 1
else:
    print("Too many failed attempts.")

    