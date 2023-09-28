print("welcome to the checkout")
height = int(input("What is your Height in cm"))

if height>120:
    print("You can buy a ticket")
    age = int(input("what is your age?"))
    if age < 12:
        print("Please pay 7$")
    elif age <= 18:
        print("Please pay 10$")
    elif age > 18:
        print("Please pay 24$")
    else:
        print("Please pay 15$")
else:
    print("Sorry, You can't buy it because the neck is small")
