import random

def CollegeChoice():
    print("Pick a college:")
    print("1.) Lorehold (Histoy)")
    print("2.) Prismari (The Arts)")
    print("3.) Quandrix (Mathematics)")
    print("4.) Silverquill (Politics)")
    print("5.) Witherbloom (Plants/Biology)")


    choice = input("> ")
    if choice == "1":
        loreholdstart()
    elif choice == "2":
        prismaristart()
    elif choice == "3":
        quandrixstart()
    elif choice == "4":
        silverquillstart()
    elif choice == "5":
        witherbloomstart()
    else:
        print("Invalid choice. Please try again")
        CollegeChoice()

def loreholdstart():
    print("You awaken in your dorm.\nVaroius books line your bookshelves. Most of which are about various civilizations across the planes.")
    print("As you exit your dorm to go to the first lecture of the day, you see an unusual door at the end of the hallway.")
    print("You know that that door wasn't there yesterday.")
    print("What do you do?")
    print("1.) Ignore the door. Maybe it will be there later")
    print("2.) Investigate the door")

    choice = input("> ")
    if choice == "1":
        lorend1()
    elif choice == "2":
        lore2()
    else:
            print("Invalid choice. Please try again")
            loreholdstart()

def lorend1():
    print("You decide to ignore the door and go to your lecture.\nWhen you get back the door is gone.\nLater you hear that one of your classmates went missing.")
    print("You later graduate with a degree in Archeology.")
    print("You have acchived a mid ending.")

def lore2():
    print("You decide that investiating this door is more important than your lecture on ancient Ravnica.")
    print("The style of door isn't recognizable to you.\nThe handle seems to be very ornate, even if it looks a bit tarnished.")
    print("What do you do now?")
    print("1.) Open the door")
    print("2.) Go to your lecture")

    choice = input("> ")
    if choice == "1":
        house1()
    elif choice == "2":
        lorend1()
    else:
        print("Invalid choice. Please try again")
        lore2()


def prismaristart():
    print("You awaken in your dorm feeling exhausted.\nLast night was particularly rough, because you stayed up until four in the morning writing a script that is due today. ")
    print("As you grab your completed script and head out the door, you see a door covered in red and blue paint at the end of the hallway.")
    print("What do you do?")
    print("1.) Go to turn in your script")
    print("2.) Investigate the door")

    choice = input("> ")
    if choice == "1":
        prisend()
    elif choice == "2":
        pris2()
    else:
        print("Invalid choice. Please try again.")
        prismaristart()


def prisend():
    print("You decide that this interesting looking door can wait for later.")
    print("You turn in your script and get an 92%.")
    print("You return to your dorm later to investigate the door and find that the door is no longer there.")
    print("You later find out that one of the teachers went missing, and the last place they were seen was in your dorm.")
    print("Maybe its best you didnt investigate the door.")
    print("You have acchived a mid ending")

def pris2():
    print("You aproach the door.")
    print("The door is covered in miniature paitings of moths.")
    print("The doorknob is very ornate.")
    print("What do you do?")
    print("1.) Open the door")
    print("2.) Go to turn in your script")

    choice = input("> ")
    if choice == "1":
        prisend()
    elif choice == "2":
        house1()
    else:
        print("Invalid choice. Please try again.")
        pris2()


def house1():
    print("You open the door.")