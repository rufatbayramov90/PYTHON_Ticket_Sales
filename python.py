'''print("welcome to the checkout")
height = int(input("What is your Height in cm"))
bill = 0
if height>120:
    print("You can buy a ticket")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5
        print("Please pay 7$")
    elif age <= 18:
        bill = 3
        print("Please pay 10$")
    elif age > 18:
        bill = 14
        print("Please pay 24$") 
    else:
        print("You did not enter the correct age Y or N")
    photo = input("Do you want a photo taken?")
    if photo == "Y":
        bill += 3 
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, You can't buy it because the neck is small")
'''


print("Would you like to buy pizza")
bill = 0
size = input("What size pizza do you want? S, M or L")
if size =="S":
    bill = 15
    print(f"Please pay ${bill}")
elif size =="M":
    bill = 20
    print(f"Please pay ${bill}")
else:
    bill = 25
    print(f"Please pay ${bill}")

add_pepperoni = input("Do you want pepperoni? Y or N")
if add_pepperoni =="Y":
    bill += 5
    print(f"Please pay ${bill}")

add_cheese = input("Do you want extra cheese? Y or N")
if add_cheese =="Y":
    bill += 10
    print(f"Please pay ${bill}")
else:
    print(f"Your final bill ${bill}")