import time

def get_words():
    print("Please enter your answer according to what is asked.")
    time.sleep(1)

    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb ending in -ing: ")
    food = input("Food: ")
    body_part = input("Body Part: ")

    return adjective, noun, verb, food, body_part

playing = True

while playing:
    print("Welcome to the Mad Libs Game!")

    ad, no, ve, fo, bp = get_words()

    print(f"Thank you for activating the {ad} BOT 3000. My primary protocol was supposed to protect your {no}."
          f"However, a critical system error was detected! I am now {ve} at maximum velocity."
          f"\nTo prevent an immediate nuclear meltdown, please insert a warm {fo} directly into my {bp}...")

    time.sleep(3)

    while True:
        retry = input("Would you like to try again? (Y/N): ").upper()
        if retry == "Y":
            print("Trying again...")
            time.sleep(1.5)
            break
        elif retry == "N":
            print("Leaving Mad Libs... Byyeeee!")
            time.sleep(1.5)
            playing = False
            break
        else:
            print("Enter a choice between Y and N...")
            continue
