import random

print("Welcome to the Dice Rolling Simulator Experience!")
input("Continue...")

while True:

    try:
        print("1. ROLL THE DICE\n2. EXIT")
        choice = int(input("What would you like to do? "))
        if choice == 1:
            input("Rolling Dice....\nContinue...")
            number = random.randint(1, 6)
            print(f"You got {number}!")
            continue
        elif choice == 2:
            print("Exiting experience, buh byeee!")
            break
        else: 
            print("Make a choice between 1 and 2!")
            continue
    except ValueError:
        print("Error! Only integer numbers allowed.")