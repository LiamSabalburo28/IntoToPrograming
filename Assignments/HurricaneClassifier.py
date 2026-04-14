def windspeed():
    try:
        ws = float(input("What is the wind speed in MPH?\n---> "))
        return ws
    except ValueError:
        print("You entered something incorrectly. Please try again.\n")
        return windspeed()

ws = windspeed()


if ws < 74:
    print("Tropical storm")
elif ws < 96:
    print("Category 1")
elif ws < 111:
    print("Category 2")
elif ws < 130:
    print("Category 3")
elif ws < 157:
    print("Category 4")
else:
    print("Category 5")