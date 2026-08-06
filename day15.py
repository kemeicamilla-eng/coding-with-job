#RECURSION
#A function that calls itself until it reaches a base case.

def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 2)

countdown(5)  # Output: 5 3 1 Blast off!

def hello(times):
    if times <= 0:
        return
    else:
        print("Hello!")
        hello(times - 1)

hello(3)  # Output: Hello! Hello! Hello!

def countdown(n):
    print(n)
    countdown(n - 1) 

def countdown(n):
    if n <= 0:
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)

countdown(10)  # Output: 5 4 3 2 1 Blast off!