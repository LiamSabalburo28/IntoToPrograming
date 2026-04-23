import random
import time
from time import sleep

def CollegeChoice():
    print("Pick a college:")
    print("1.) Lorehold (Histoy)")
    print("2.) Prismari (The Arts)")
    print("3.) Quandrix (Mathematics)")
    print("4.) Silverquill (Politics/Law)")
    print("5.) Witherbloom (Plants/Biology)")

    choice = input("> ")
    if choice == "1":
        loreholdstart() #sends to the start of the lorehold storyline
    elif choice == "2":
        prismaristart() # sends to the start of the prismari storyline
    elif choice == "3":
        quandrixstart() #sends to the start of the quandrix storyline
    elif choice == "4":
        silverquillstart() # sends to the start of the silverquil storyline
    elif choice == "5":
        witherbloomstart() #sends to the start of the witherbloom storyline
    elif choice == "developer options":
        devop()
    else:
        print("Invalid choice. Please try again") #restarts the function if an answer not defined is chosen
        CollegeChoice()

def devop():
    print("Just kidding. There are no developer options.")
    sleep(10); print("""
888                                
888                                
888                                
888 .d88b. .d8888b  .d88b. 888d888 
888d88""88b88K     d8P  Y8b888P"   
888888  888"Y8888b.88888888888     
888Y88..88P     X88Y8b.    888     
888 "Y88P"  88888P' "Y8888 888    
""")


def loreholdstart():
    print("You awaken in your dorm.\nVaroius books line your bookshelves. Most of which are about various civilizations across the planes.")
    print("As you exit your dorm to go to the first lecture of the day, you see an unusual door at the end of the hallway.")
    print("You know that that door wasn't there yesterday.")
    print("What do you do?")
    print("1.) Ignore the door. Maybe it will be there later")
    print("2.) Investigate the door")

    choice = input("> ")
    if choice == "1": # if 1 is chosen, sends to the end of the lorehold storyline
        lorend1()
    elif choice == "2":
        loredoor() # if 3 is chosen, sends to the second part of the lorehold storyline
    else:
            print("Invalid choice. Please try again")
            loreholdstart()

def lorend1():
    print("You decide to ignore the door and go to your lecture.\nWhen you get back the door is gone.\nLater you hear that one of your classmates went missing.")
    print("You later graduate with a degree in Archeology.")
    print("You have acchived a mid ending.") # ending of the lorehold storyline

def loredoor():
    print("You decide that investiating this door is more important than your lecture on ancient Ravnica.")
    print("The style of door isn't recognizable to you.\nThe handle seems to be very ornate, even if it looks a bit tarnished.")
    print("What do you do now?")
    print("1.) Open the door")
    print("2.) Go to your lecture")

    choice = input("> ")
    if choice == "1":
        house1() # sends to the start of the house
    elif choice == "2":
        lorend1() #sends to the end of the lorehold storyline
    else:
        print("Invalid choice. Please try again")
        loredoor()


def prismaristart():
    print("You awaken in your dorm feeling exhausted.\nLast night was particularly rough, because you stayed up until four in the morning writing a script that is due today. ")
    print("As you grab your completed script and head out the door, you see a door covered in red and blue paint at the end of the hallway.")
    print("What do you do?")
    print("1.) Go to turn in your script")
    print("2.) Investigate the door")

    choice = input("> ")
    if choice == "1":
        prisend() # sends to the end of the prismari storyline
    elif choice == "2":
        prisdoor() # sends to the second part of the prismari storyline
    else:
        print("Invalid choice. Please try again.")
        prismaristart()

def prisend():
    print("You decide that this interesting looking door can wait for later.")
    print("You turn in your script and get an 92%.")
    print("You return to your dorm later to investigate the door and find that the door is no longer there.")
    print("You later find out that one of the teachers went missing, and the last place they were seen was in your dorm.")
    print("Maybe its best you didnt investigate the door.")
    print("You have acchived a mid ending") # end of the prismari storyline

def prisdoor():
    print("You aproach the door.")
    print("The door is covered in miniature paitings of moths.")
    print("The doorknob is very ornate.")
    print("What do you do?")
    print("1.) Open the door")
    print("2.) Go to turn in your script")

    choice = input("> ")
    if choice == "1":
        prisend() # sends to the end of the prismari storyline
    elif choice == "2":
        house1() # sends to the beginning of the house storyline
    else:
        print("Invalid choice. Please try again.")
        prisdoor()


def quandrixstart():
    print("You awaken at your desk surrounded by your textbooks. You check the time and realize you have about 30 minutes to get to the first lecture of the day.")
    print("As you rush out of your dorm you see a door at the end of the hallway.")
    print("Do you,")
    print("A.) Investigate the door")
    print("B.) Go to your lecture")

    choice = input("> ")
    if choice == "A":
        quanddoor() # sends to the second part of the quandrix storyline
    elif choice == "B":
        quandrixend()
    else:
        print("Invalid choice. Pleas try again.")
        quandrixstart()

def quanddoor():
    print("You go up to the door and decide to investigate. The door appears to match the other doors lading into your classmates dorms.")
    print("What do you do?")
    print("1.) Go to your lecture")
    print("2.) Open the door")

    choice = input("> ")
    if choice == "1":
        quandrixend() # sends to the end of the quandrix storyline
    elif choice == "2":
        house1() # sends to the house storyline
    else:
        print("Invalid choice. Please try again")
        quanddoor()

def quandrixend():
    print("You decide to ignore the door and head to your lecture. As you are rushing down the stairs, you miss a step and tumble down the stairs.\nYou end up breaking your neck and die.")
    print("YOU HAVE DIED") # ending for the quandrix storyline
    sleep(5); print("""
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡖⠖⠎⠍⢭⢫⣋⡋⡗⣒⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣖⣯⣷⣥⣶⢪⣿⢛⡅⣇⣷⢫⡟⣰⣯⣔⡩⡑⠢⣄⠀⠀⠀
⠀⠀⠀⡜⢹⣯⣟⣻⢹⣏⢿⡻⡷⣫⡯⡟⣽⣷⣕⣓⡚⢙⢲⡗⡌⢧⡀⠀
⠀⠀⢠⠷⣿⣝⣗⡿⣷⡳⣏⡏⢥⠆⡷⡖⢭⣮⣧⣬⣶⣟⣾⢬⡿⡆⣣⠃
⠀⢀⣸⢀⢿⠟⣿⣟⡗⡣⡾⣗⢄⣛⠱⣯⣽⠟⣜⣍⢪⡽⢯⣙⣧⠄⢼⡆
⠀⠀⡇⣽⡻⠛⡿⠡⠭⠥⡥⣍⠒⡙⢻⣇⠛⢋⢛⣋⣋⣗⠓⠞⢛⣢⣻⢱
⠀⠁⡯⣿⣕⡛⠆⠀⠀⠀⠀⠈⢳⢹⡷⡏⠁⠉⢃⢟⡂⠀⠀⠀⠀⠈⢩⣸
⠀⢤⣋⡗⣇⣢⠀⠀⠸⣯⣢⡄⠈⢐⡇⠇⠀⠀⢆⡺⡆⢠⢻⣷⡇⠀⢱⣸
⠀⡝⡿⡿⠴⣘⠀⠀⠀⠀⣤⣀⡁⡜⡇⡃⠀⠀⢃⢴⡃⠈⠉⠉⠁⠀⢸⢼
⠀⣷⣇⡟⡇⡫⠀⠀⠀⡄⠀⠙⠳⣗⠃⡅⠀⠀⢅⣛⡇⠀⠀⡆⢔⡆⢹⢸
⠀⡯⣬⣇⣛⡇⠀⠀⠀⡗⣆⠀⠨⠷⡑⠄⠀⠀⢂⣻⡁⠀⠀⠣⡁⡆⣾⢸
⠀⡇⢧⡇⡶⡗⡂⠂⡦⣏⣻⣆⣀⠠⢛⡄⠀⠀⠅⡧⡀⠀⠀⣃⢂⡂⣵⢨
⠀⡗⣻⢟⣻⡻⡧⣇⣶⢪⣽⣯⢯⣷⡷⣏⣝⣍⡏⣏⣃⣐⢀⣳⣽⣦⣉⢸
⠀⡗⣞⡍⡏⠜⢭⠙⢎⣿⣿⣟⣃⢃⣕⣹⢽⣿⠿⡿⢻⡟⠿⣯⢿⠏⠍⢰
⠀⡇⢚⡆⣻⠎⢂⡃⣠⢌⢓⠡⡂⡀⡦⡛⢘⡲⣋⣹⢐⢇⡷⠟⣭⠳⠣⢸
⠀⡗⢦⡍⢷⠇⠂⠘⠸⣇⣏⢆⡴⣁⠄⣹⡏⠄⢵⢴⣂⡫⢘⣉⣰⠆⡁⢸
⠀⡂⢯⢨⠯⠘⢒⡿⡥⣛⣡⡒⡱⣶⣂⡏⣓⡜⢖⠜⣧⣋⣽⡖⣧⡃⡂⢸
⠀⣒⠭⢍⢃⠀⡉⡏⢗⡷⣺⡷⡎⠂⣆⡁⣒⡖⡰⣱⠧⢆⢅⣢⣟⡿⡁⢸
⠀⣽⡇⡲⢀⣋⣇⢹⣗⣠⣌⡈⣲⣁⣆⡽⣃⣔⢅⣭⣙⣭⢞⡙⡝⠬⠄⢸
⠒⠊⠁⡟⠨⢝⢓⢛⣤⡂⣁⠤⡉⡁⢅⠁⡡⢀⠍⣍⠡⢋⡥⣍⡈⠁⠁⢘
""")


def silverquillstart():
    print("You wake up in your bed in your silk pajamas. Today you have an in class debate about the ethics of using constructs for labour. As you have your perfectly made breakfast with your perfectly made coffee, you review your notes on the debate.")
    print("As you walk out the door and head ot the assigned lecture hall, you see a ornate looking door at the end of the hallway.")
    print("What do you do?")
    print("1.) Investigate the door")
    print("2.) Head to the debate")

    choice = input("> ")
    if choice == "1":
        silverdoor() # sends to the second part of the silverquill storyline
    elif choice == "2":
        silverend() # sends to the end of the silverquill storyline
    else:
        print("Invalid choice. Please try again.")
        silverquillstart()

def silverdoor():
    print("The door appears to be made of mahogany. The doorknob is made out of mithril.")
    print("What do you do?")
    print("1.) Go to your lecture")
    print("2.) Open this really nice door")

    choice = input("> ")
    if choice == "1":
        silverend() # sends to the end of the silverquill storyline
    elif choice == "2":
        house1() # sends to the beginning of the house storyline
    else:
        print("Invalid choice. Please try again")
        silverdoor()

def silverend():
    print("You decide to ignore the door. You head to your debate and absolutley destroy your opponent.")
    print("You have acchived the debatable ending.") # end of the silverquill ending
              


def witherbloomstart():
    print("You awaken in your hammock. The entierty of your dorm is covered in plants from all accross the planes.")
    print("As you get ready to head to your first demonstration of the day, you see a door at the end of the hallway.")
    print("What do you do?")
    print("1.) Investigate the door")
    print("2.) Go to your demonstration")

    choice = input("> ")
    if choice == "1":
        witherdoor() # sends to the second part of the witherbloom storyline
    elif choice == "2":
        witherend() # sends to the end of the witherbloom storyline
    else:
        print("Invalid choice. Please try again.")
        witherbloomstart()

def witherdoor():
    print("The door appears to be made of a rotting oak, and the knob is made of nickle. There also appears to be Death's Head Hawkmoths painted on the wood.")
    print("What do you do?")
    print("1.) Go to the demonstration")
    print("2.) Open the door")

    choice = input("> ")
    if choice == "1":
        witherend() # sends to the end of the witherbloom storyline
    elif choice == "2":
        house1() # sends to the beginning of the house storyline
    else:
        print("Invalid choice. Please try again.")
        witherdoor()

def witherend():
    print("You decide to ignore the door. You later are poisoned by your rival and die.")
    print("You have achived the poisoned ending")





def house1():
    print("You open the door. Inside is an abandoned hallway. On the walls are pictures of a happy family.")
    print("What do you do?")
    print("1.) Proceed")
    print("2.) Thats an ominous looking hallway, I'm not going in.")

    choice = input("> ")
    if choice == "1":
        house2()
    elif choice == "2":
        forcedenter()
    else:
        print("Invalid choice. Please try again.")
        house1()

def house2():
    print("As you proceed farther into the hallway, the faces in the pictures begin to melt.")
    sleep (3); print("The door suddenly slams shut.")
    print("As you travel down the hallway you come to a three way for in the hallway.")
    sleep (1); print("Which way do you go?")
    print("1.) North")
    print("2.) East")
    print("3.) South")
    print("4.) West")

    choice = input("> ")
    if choice == "1":
        elevator()
    elif choice == "2":
        office()
    elif choice == "3":
        sauna()
    elif choice == "4":
        lockerroom()
    else:
        print("Invalid choice. Please try again.")
        house2()

def forcedenter():
    print("The door suddenly slams shut and vanishes right before your eyes.")
    print("Do you go,")
    print("1.) Forward")
    print("2.) Backward")

    choice = input("> ")

    if choice == "1":
        house2
    elif choice == "2":
        house2()
    else:
        print("Invalid choice. Try again")
        forcedenter()

def fork():
    print("You return to the fork in the hallway.")
    print("Which way do you go?")
    print("1.) North")
    print("2.) East")
    print("2.) East")
    print("3.) South")
    print("4.) West")

    choice = input("> ")
    if choice == "1":
        elevator()
    elif choice == "2":
        office()
    elif choice == "3":
        sauna()
    elif choice == "4":
        lockerroom()
    else:
        print("Invalid choice. Please try again.")
        fork()



def elevator():
    print("You choose to go north.")
    sleep(5); print("After about three minutes of walking, you come upon an elevator and some stairs.")
    print("Which one will you take?")
    sleep(1); print("Elevator")
    sleep(1); print("Stairs")
    sleep(1); print("Look for another door (Type 3)")
    
    choice = input("> ")
    if choice == "elevator":
        escape()
    elif choice == "Elevator":
        escape()
    elif choice == "stairs":
        stairescape()
    elif choice == "Stairs":
        stairescape()
    elif choice == "3":
        elevatorhallway()
    else:
        print("Invalid choice. Please try again.")
        elevator()

def escape():
    print("You enter the elevator and press a random button.")
    print("After a while the doors open and you step back out into your dorm hallway.")
    sleep(3); print("You are confused as to what exactly happened, and never figure out where you were or where that strange house was.")
    print("You survived The House.")
    print("You have acchived the survivor ending.")

def stairescape():
    print("You climb the stairs.")
    sleep(2); print("After a while the stairs change from rotting wood to the stairs back in your dorm.")
    print("As you get to the top of the stairs they dissapear.")
    sleep(3); print("You are confused as to what exactly happened, and never figure out where you were or where that strange house was.")
    print("You survived The House.")
    print("You have acchived the survivor ending.")

def elevatorhallway():
    print("You find two doors.")
    print("What will you do?")
    print("1.) Take the left door")
    print("2.) Take the right door")
    print("3.) Go back to the fork")
    print("4.) Take the elevator")
    print("5.) Take the stairs")

    choice = input("> ")
    if choice == "1":
        idkwhatleftdooris()
    elif choice == "2":
        idkwhatrightdooris()
    elif choice == "3":
        fork()
    elif choice == "4":
        escape()
    elif choice == "5":
        stairescape()
    else:
        print("Invalid choice. Please try again")
        elevatorhallway()
    

def lockerroom():
    print("As you turn left you enter what looks like an abandoned locker room for a pool.")
    sleep(1); print("The stench of chlorine fills the air. At the other end of the locker room is a door, probably leading to a pool.")
    print("What do you do?")
    print("1.) Head back to the hallway")
    print("2.) Head to the pool")
    print("3.) Attempt to open a locker")

    choice = input("> ")
    if choice == "1":
        house2()
    elif choice == "2":
        pool()
    elif choice == "3":
        locker()
    else:
        print("Invalid choice. Try again")
        lockerroom()

def locker():
    print("You go to a locker and it appears to be locked with a number lock.")
    print("What do you do?")
    print("1.) Go to the pool")
    print("2.) Open the locker")
    print("3.) Leave the locker room")

    choice = input("> ")
    if choice == "1":
        pool()
    elif choice == "2":
        lockerpuzzle()
    elif choice =="3":
        fork()
    else:
        print("Invalid choice. Please try again.")
        locker()

def pool():
    print("You push open the door and find an olympic sized pool")
    print("What do you do?")
    print("1.) Go swimming")
    print("2.) Check the water")
    print("3.) Go back to the fork")

    choice = input("> ")
    if choice == "1":
        poolend()
    elif choice == "2":
        poolcheck()
    elif choice == "3":
        fork()
    else:
        print("Invalid choice. Please try again.")
        pool()

def lockerpuzzle():
    print("The locker you stopped in front of has a three number lock.")
    print("What is the code?")
    print("1.) 18-36-11")
    print("2.) 22-01-33")
    print("3.) 05-09-16")
    print("4.) 06-06-06")

    choice = input("> ")
    if choice == "1":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "2":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "3":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "4":
        print("The lock opened")
        openlocker()
    elif choice == "open":
        sleep(10); print("You are sneaky. I'll open the locker this time...")
        openlocker()
    else:
        print("Invalid choice. Please try again.")
        lockerpuzzle()
        
def yesno():
    answer = input("> ")
    if answer == "yes":
            locker2()
    elif answer == "no":
            no()
    else:
            print("Invalid choice. Please try again.")

def no():
        print("What will you do now?")
        print("1.) Go to the pool")
        print("2.) Go back to the fork")
        option = input("> ")
        if option == "1":
            pool()
        elif option == "2":
            fork()
        else:
            print("Invalid choice. Please try again.")
            no()

def openlocker():
    print("You open the locker and can't find ", end="", flush=True)

    text = "y o u r   h a n d"
    for char in text:
        print(char, end="", flush=True)
        time.sleep(1)
        

def locker2():
    print(" You stand in front of the locker, attempting to figure out the combination.")
    print("What is the code?")
    print("1.) 18-36-11")
    print("2.) 22-01-33")
    print("3.) 05-09-16")
    print("4.) 06-06-06")

    choice = input("> ")
    if choice == "1":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "2":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "3":
        print("The lock didnt budge.")
        print("Try again? (yes or no)")
        yesno()
    elif choice == "4":
        print("The lock opened")
        openlocker()
    elif choice == "open":
        sleep(10); print("You are sneaky. I'll open the locker this time...")
        openlocker()
    else:
        print("Invalid choice. Please try again.")
        locker2()

def poolend():
    print("You jump in the pool. You failed to notice that the pool has sharks in it.")
    sleep(2); print("You are eaten by the sharks.")
    print("You have died.")
    sleep(2); print("""
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡖⠖⠎⠍⢭⢫⣋⡋⡗⣒⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣖⣯⣷⣥⣶⢪⣿⢛⡅⣇⣷⢫⡟⣰⣯⣔⡩⡑⠢⣄⠀⠀⠀
⠀⠀⠀⡜⢹⣯⣟⣻⢹⣏⢿⡻⡷⣫⡯⡟⣽⣷⣕⣓⡚⢙⢲⡗⡌⢧⡀⠀
⠀⠀⢠⠷⣿⣝⣗⡿⣷⡳⣏⡏⢥⠆⡷⡖⢭⣮⣧⣬⣶⣟⣾⢬⡿⡆⣣⠃
⠀⢀⣸⢀⢿⠟⣿⣟⡗⡣⡾⣗⢄⣛⠱⣯⣽⠟⣜⣍⢪⡽⢯⣙⣧⠄⢼⡆
⠀⠀⡇⣽⡻⠛⡿⠡⠭⠥⡥⣍⠒⡙⢻⣇⠛⢋⢛⣋⣋⣗⠓⠞⢛⣢⣻⢱
⠀⠁⡯⣿⣕⡛⠆⠀⠀⠀⠀⠈⢳⢹⡷⡏⠁⠉⢃⢟⡂⠀⠀⠀⠀⠈⢩⣸
⠀⢤⣋⡗⣇⣢⠀⠀⠸⣯⣢⡄⠈⢐⡇⠇⠀⠀⢆⡺⡆⢠⢻⣷⡇⠀⢱⣸
⠀⡝⡿⡿⠴⣘⠀⠀⠀⠀⣤⣀⡁⡜⡇⡃⠀⠀⢃⢴⡃⠈⠉⠉⠁⠀⢸⢼
⠀⣷⣇⡟⡇⡫⠀⠀⠀⡄⠀⠙⠳⣗⠃⡅⠀⠀⢅⣛⡇⠀⠀⡆⢔⡆⢹⢸
⠀⡯⣬⣇⣛⡇⠀⠀⠀⡗⣆⠀⠨⠷⡑⠄⠀⠀⢂⣻⡁⠀⠀⠣⡁⡆⣾⢸
⠀⡇⢧⡇⡶⡗⡂⠂⡦⣏⣻⣆⣀⠠⢛⡄⠀⠀⠅⡧⡀⠀⠀⣃⢂⡂⣵⢨
⠀⡗⣻⢟⣻⡻⡧⣇⣶⢪⣽⣯⢯⣷⡷⣏⣝⣍⡏⣏⣃⣐⢀⣳⣽⣦⣉⢸
⠀⡗⣞⡍⡏⠜⢭⠙⢎⣿⣿⣟⣃⢃⣕⣹⢽⣿⠿⡿⢻⡟⠿⣯⢿⠏⠍⢰
⠀⡇⢚⡆⣻⠎⢂⡃⣠⢌⢓⠡⡂⡀⡦⡛⢘⡲⣋⣹⢐⢇⡷⠟⣭⠳⠣⢸
⠀⡗⢦⡍⢷⠇⠂⠘⠸⣇⣏⢆⡴⣁⠄⣹⡏⠄⢵⢴⣂⡫⢘⣉⣰⠆⡁⢸
⠀⡂⢯⢨⠯⠘⢒⡿⡥⣛⣡⡒⡱⣶⣂⡏⣓⡜⢖⠜⣧⣋⣽⡖⣧⡃⡂⢸
⠀⣒⠭⢍⢃⠀⡉⡏⢗⡷⣺⡷⡎⠂⣆⡁⣒⡖⡰⣱⠧⢆⢅⣢⣟⡿⡁⢸
⠀⣽⡇⡲⢀⣋⣇⢹⣗⣠⣌⡈⣲⣁⣆⡽⣃⣔⢅⣭⣙⣭⢞⡙⡝⠬⠄⢸
⠒⠊⠁⡟⠨⢝⢓⢛⣤⡂⣁⠤⡉⡁⢅⠁⡡⢀⠍⣍⠡⢋⡥⣍⡈⠁⠁⢘
""")
    
def poolcheck():
    print("As you look into the pool you can see sharks swimming in the pool.")
    print("What do you do?")
    print("1.) Jump in the pool, despite the fact that there are sharks.")
    print("2.) Go back to the fork")
    print("3.) Look for another door")

    choice = input("> ")
    if choice =="1":
        pooldeath()
    elif choice == "2":
        fork()
    elif choice == "3":
        pooltwodoor()
    else:
        print("Invalid choice. Please try again.")
        poolcheck()

def pooldeath():
    print("You jump in the pool. Ignoring the fact that there are sharks in the pool.")
    sleep(2); print("You are eaten by said sharks.")
    print("You have died.")
    sleep(2); print("""
⠀⠀⠀⠀⠀⠀⠀⣀⣤⡖⠖⠎⠍⢭⢫⣋⡋⡗⣒⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣖⣯⣷⣥⣶⢪⣿⢛⡅⣇⣷⢫⡟⣰⣯⣔⡩⡑⠢⣄⠀⠀⠀
⠀⠀⠀⡜⢹⣯⣟⣻⢹⣏⢿⡻⡷⣫⡯⡟⣽⣷⣕⣓⡚⢙⢲⡗⡌⢧⡀⠀
⠀⠀⢠⠷⣿⣝⣗⡿⣷⡳⣏⡏⢥⠆⡷⡖⢭⣮⣧⣬⣶⣟⣾⢬⡿⡆⣣⠃
⠀⢀⣸⢀⢿⠟⣿⣟⡗⡣⡾⣗⢄⣛⠱⣯⣽⠟⣜⣍⢪⡽⢯⣙⣧⠄⢼⡆
⠀⠀⡇⣽⡻⠛⡿⠡⠭⠥⡥⣍⠒⡙⢻⣇⠛⢋⢛⣋⣋⣗⠓⠞⢛⣢⣻⢱
⠀⠁⡯⣿⣕⡛⠆⠀⠀⠀⠀⠈⢳⢹⡷⡏⠁⠉⢃⢟⡂⠀⠀⠀⠀⠈⢩⣸
⠀⢤⣋⡗⣇⣢⠀⠀⠸⣯⣢⡄⠈⢐⡇⠇⠀⠀⢆⡺⡆⢠⢻⣷⡇⠀⢱⣸
⠀⡝⡿⡿⠴⣘⠀⠀⠀⠀⣤⣀⡁⡜⡇⡃⠀⠀⢃⢴⡃⠈⠉⠉⠁⠀⢸⢼
⠀⣷⣇⡟⡇⡫⠀⠀⠀⡄⠀⠙⠳⣗⠃⡅⠀⠀⢅⣛⡇⠀⠀⡆⢔⡆⢹⢸
⠀⡯⣬⣇⣛⡇⠀⠀⠀⡗⣆⠀⠨⠷⡑⠄⠀⠀⢂⣻⡁⠀⠀⠣⡁⡆⣾⢸
⠀⡇⢧⡇⡶⡗⡂⠂⡦⣏⣻⣆⣀⠠⢛⡄⠀⠀⠅⡧⡀⠀⠀⣃⢂⡂⣵⢨
⠀⡗⣻⢟⣻⡻⡧⣇⣶⢪⣽⣯⢯⣷⡷⣏⣝⣍⡏⣏⣃⣐⢀⣳⣽⣦⣉⢸
⠀⡗⣞⡍⡏⠜⢭⠙⢎⣿⣿⣟⣃⢃⣕⣹⢽⣿⠿⡿⢻⡟⠿⣯⢿⠏⠍⢰
⠀⡇⢚⡆⣻⠎⢂⡃⣠⢌⢓⠡⡂⡀⡦⡛⢘⡲⣋⣹⢐⢇⡷⠟⣭⠳⠣⢸
⠀⡗⢦⡍⢷⠇⠂⠘⠸⣇⣏⢆⡴⣁⠄⣹⡏⠄⢵⢴⣂⡫⢘⣉⣰⠆⡁⢸
⠀⡂⢯⢨⠯⠘⢒⡿⡥⣛⣡⡒⡱⣶⣂⡏⣓⡜⢖⠜⣧⣋⣽⡖⣧⡃⡂⢸
⠀⣒⠭⢍⢃⠀⡉⡏⢗⡷⣺⡷⡎⠂⣆⡁⣒⡖⡰⣱⠧⢆⢅⣢⣟⡿⡁⢸
⠀⣽⡇⡲⢀⣋⣇⢹⣗⣠⣌⡈⣲⣁⣆⡽⣃⣔⢅⣭⣙⣭⢞⡙⡝⠬⠄⢸
⠒⠊⠁⡟⠨⢝⢓⢛⣤⡂⣁⠤⡉⡁⢅⠁⡡⢀⠍⣍⠡⢋⡥⣍⡈⠁⠁⢘
""")

def pooltwodoor():
    print("It takes you a while but you eventually you find a door that leads to another hallway.")
    sleep(1); print("You travel along this hallway for about ten minutes before the path splits off.")
    print("Which way will you go?")
    print("1.) Left")
    print("2.) Right")

    choice = input("> ")
    if choice == "1":
        salon()
    elif choice == "2":
        valgavoth()
    else:
        print("Invalid choice. Please try again.")
        pooltwodoor()


def salon():
    print("You push open the left door and find yourself in a lounge.")
    print("Various bottles line the shelves.")
    print("What do you do?")
    print("1.) Investigate the bottles")
    print("2.) Grab a bottle and chug it")
    print("3.) Go back to the pool")
    print("4.) Lie down on one of the couches")

    choice = input("> ")
    if choice == "1":
        investigatebottle()
    elif choice == "2":
        bottledeath()
    elif choice == "3":
        pool()
    elif choice == "4":
        couchdeath()
    else:
        print("Invalid choice. Please try again")

def investigatebottle():
    print("On one of the bottles is labeled Aqua Tofana. As you look at more bottles you realize that they are poisons.")
    print("Good thing you didn't drink any.")
    print("What do you do now?")
    print("1.) Go back to the pool")
    print("2.) Go lie down on one of the couches")

    choice = input("> ")
    if choice == "1":
        pool()
    elif choice == "2":
        couchdeath()
    else:
        print("Invalid option. Please try again.")
        investigatebottle()

def bottledeath():
    print("You start to chug one of the bottles. What could possibly go wrong?")
    sleep(2); print("You soon find out what could possibly go wrong.")
    print("The bottle contained poison.")
    print("At least you died quickly...")

def couchdeath():
    print("You lay down on one of the couches. It's supprisingly comfy.")
    print("You close your eyes,")
    sleep(5); print("and you don't wake up again")

    


CollegeChoice()