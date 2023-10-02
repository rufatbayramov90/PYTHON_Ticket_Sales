print("welcome to the checkout")
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
