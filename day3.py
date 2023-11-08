print("Welcome to the rollercoaster")
name = int(input("enter the height"))
age = int(input("enter the age"))

if name >= 120:
    if age >18:
        print("pay 12 dollors")
    elif age >=12 & age <= 18:
        print("you got $7")
    else:
        print("you got 5 dollar")
else:
    print("sorry")
    