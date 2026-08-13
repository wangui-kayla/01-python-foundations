import time
import random

playing = True

def play_round():
    options = ["ROCK", "PAPER", "SCISSORS"]

    while True:

        print("1. ROCK\n2. PAPER\n3. SCISSORS")

        player_choice = input("Type your choice (ROCK, PAPER or SCISSORS): ").upper()

        if player_choice not in options:
            print("Error! Please choose ROCK, PAPER or SCISSORS.")
            continue

        break

    computer_choice = random.choice(options)

    beats = {
        "ROCK" : "SCISSORS",
        "PAPER" : "ROCK",
        "SCISSORS" : "PAPER"
    }

    if player_choice == computer_choice:
        print(f"You chose: {player_choice}\nComputer chose: {computer_choice}")
        time.sleep(1)
        print("YOU TIE!!")
        return "tie"
    elif beats[player_choice] == computer_choice:
        print(f"You chose: {player_choice}\nComputer chose: {computer_choice}")
        time.sleep(1)
        print("YOU WIN!!")
        return "win"
    elif beats[computer_choice] == player_choice:
        print(f"You chose: {player_choice}\nComputer chose: {computer_choice}")
        time.sleep(1)
        print("YOU LOSE!!")
        return "lose"

win = 0
lose = 0
tie = 0

while playing:
    print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME!")
    time.sleep(1)

    result = play_round()

    if result == "tie":
        tie += 1
    elif result == "win":
        win += 1
    elif result == "lose":
        lose += 1

    print("--------------------")
    print("YOUR SCORE")
    print("--------------------")
    time.sleep(1)
    print(f"WINS: {win}")
    print(f"LOSSES: {lose}")
    print(f"DRAWS: {tie}")

    time.sleep(1)
    retry = input("Would you like to play again? (Y/N): ").upper()

    if retry == "Y":
        print("Getting back to game...")
        time.sleep(2)
        continue
    elif retry == "N":
        print("Exiting game. Buh Byeeee!")
        time.sleep(2)
        playing = False