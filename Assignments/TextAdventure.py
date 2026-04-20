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

def lorend1():
    print("You decide to ignore the door and go to your lecture.\nWhen you get back the door is gone.\nLater you hear that one of your classmates went missing.")
    print("You later graduate with a degree in Archeology.")
    print("You have acchived a mid ending.")

def lore2():
    print("You decide that investigating this door is more important than your lecture.")
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