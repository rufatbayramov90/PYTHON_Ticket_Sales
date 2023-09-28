print("welcome to the checkout")
height = int(input("What is your Height in cm"))

if height>120:
    print("You can buy a ticket")
    age = int(input("what is your age?"))
    if age<=18:
        print("Please pay 10$")
    else:
        print("Please pay 15$")
else:
    print("Sorry, You can't buy it because the neck is small")
