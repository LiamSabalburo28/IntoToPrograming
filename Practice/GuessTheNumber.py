import random

target_number = random.randint(1, 100)
guess = None

print("I'm thinking of a number between 1 and 100...")

while guess != target_number:
    try:
        guess = int(input("Enter your guess: "))

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number!")

    except ValueError:
        print("Please enter a valid integer.")