windspeed = float(input("What is the wind speed in MPH?\n"))

if windspeed < 74:
    print("Tropical storm")
elif windspeed < 96:
    print("Category 1")
elif windspeed < 111:
    print("Category 2")
elif windspeed < 130:
    print("Category 3")
elif windspeed < 157:
    print("Category 4")
else:
    print("Category 5")