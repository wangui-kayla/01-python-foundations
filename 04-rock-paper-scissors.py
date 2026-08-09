import time
import random
         
print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME!")
time.sleep(1)
print("You will play rock, paper, scissors against the computer!")

options = ["ROCK", "PAPER", "SCISSORS"]

while True:
    try:
        pc_choice = random.choice(options)

        print("1. ROCK\n2. PAPER\n3. SCISSORS\n4. EXIT")
        choice = input("Type your choice (ROCK, PAPER, SCISSORS or EXIT): ").upper()

        if pc_choice == "ROCK" and choice == "SCISSORS":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU LOSE!")
            time.sleep(1.5)
            continue

        elif pc_choice == "SCISSORS" and choice == "ROCK":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU WIN!")
            time.sleep(1.5)
            continue

        elif pc_choice == "SCISSORS" and choice == "PAPER":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU LOSE!")
            time.sleep(1.5)
            continue

        elif pc_choice == "PAPER" and choice == "SCISSORS":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU WIN!")
            time.sleep(1.5)
            continue

        elif pc_choice == "PAPER" and choice == "ROCK":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU LOSE!")
            time.sleep(1.5)
            continue

        elif pc_choice == "ROCK" and choice == "PAPER":
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("YOU WIN!")
            time.sleep(1.5)
            continue

        elif pc_choice == choice:
            print(f"You chose: {choice}\nComputer chose: {pc_choice}")
            time.sleep(1)
            print("IT'S A TIE!")
            time.sleep(1.5)
            continue

        elif choice == "EXIT":
            print("Exiting Game...\nBuh Byyeeee!")
            time.sleep(1.5)
            break

        else: 
            print("Error! Please type in caps between ROCK, PAPER and SCISSORS!")
            time.sleep(1.5)
            continue

    except ValueError as e:
        print(f"Error! {e}")
        time.sleep(1.5)