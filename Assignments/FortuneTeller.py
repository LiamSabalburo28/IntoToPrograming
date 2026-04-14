import random

def fortune_teller():
    print("Welcome to the Fortune Teller!\n")

    try:
        lucky_number = int(input("Enter your lucky number (integer): "))
        years_future = float(input("How many years into the future? (float): "))
        multiplier = float(input("Enter a magical multiplier (float): "))

    except ValueError:
        print("\nInvalid input! Please enter numbers only.\n")
        fortune_teller()  
        return


    random_number = random.randint(1, 10)


    fortune_score = lucky_number * multiplier + years_future + random_number


    print("\nYour fortune is being revealed...\n")

    if fortune_score < 20:
        print("A calm and peaceful time is ahead.")
    elif fortune_score < 40:
        print("Something bad is coming your way.")
    elif fortune_score < 60:
        print("A big decision will shape your future.")
    elif fortune_score < 80:
        print("You will fail a class.")
    else:
        print("Great things are destined for you!")


fortune_teller()