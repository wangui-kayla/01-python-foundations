import random
import time

def guess_round(computer_guess):
    tries = 0
    while True:
        try:
            player_guess = int(input("Enter an integer number between 1 and 100: "))
        except ValueError as e:
            print(f"Error! {e}")
            continue

        if player_guess < 1 or player_guess > 100:
            print("Error! The number you entered is outside the range of 1 - 100.")
            continue
        elif player_guess == computer_guess:
            tries += 1
            print(f"Correct!\nYou guessed: {computer_guess}, in {tries} number of times!")
            time.sleep(1.5)
            return
        elif player_guess > computer_guess:
            tries += 1
            print("Too High!")
            time.sleep(1)
            continue
        elif player_guess < computer_guess:
            tries += 1
            print("Too Low!")
            time.sleep(1)
            continue

playing = True

while playing:
    computer_guess = random.randint(1, 100)

    print("WELCOME TO THE NUMBER GUESSING GAME!")
    time.sleep(1)

    guess_round(computer_guess)

    while True:
        retry = input("Would you like to play again? (Y/N): ").upper()
        if retry == "Y":
            print("Returning to game...")
            time.sleep(2)
            break
        elif retry == "N":
            print("Exiting game... Buh byyeeee!")
            time.sleep(2)
            playing = False
            break
        else:
            print("Enter a valid answer between Y and N.")
            continue