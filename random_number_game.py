import random

secret_number = random.randint(1, 100)
attempts = 0

print("=== GAME HUB ===")

print("I have selected a secret number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your number:"))

    attempts +=1

    if guess < secret_number:
       print("Too low. Try again")

    elif guess > secret_number:
         print("Too high. Try again")

    else:
        print("\n Congratulations!!!")
        print(f"The number was{secret_number}")
        print(f"You made{attempts} attempts.")
        break


    