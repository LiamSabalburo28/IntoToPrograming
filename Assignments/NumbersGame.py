import random
import os

LEADERBOARD_FILE = "leaderboard.txt"

def load_leaderboard():
    scores = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for line in file:
                name, attempts = line.strip().split(",")
                scores.append((name, int(attempts)))
    return sorted(scores, key=lambda x: x[1])

def save_score(name, attempts):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{name},{attempts}\n")

def display_leaderboard():
    scores = load_leaderboard()
    print("\nLeaderboard")
    print("-" * 20)
    if not scores:
        print("No scores yet.")
    else:
        for i, (name, attempts) in enumerate(scores[:10], start=1):
            print(f"{i}. {name} - {attempts} guesses")
    print("-" * 20)

def play_game():
    number = random.randint(1, 1000)
    attempts = 0

    print("Guess the number between 1 and 1000")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Higher")
            elif guess > number:
                print("Lower")
            else:
                print(f"Correct! You guessed the number in {attempts} attempts.")
                return attempts
        except ValueError:
            print("Please enter a valid number.")

def main():
    display_leaderboard()

    name = input("Enter your name: ")
    attempts = play_game()

    save_score(name, attempts)

    print("\nUpdated Leaderboard")
    display_leaderboard()

if __name__ == "__main__":
    main()