print("Welcome User!")
input("Press Enter to continue...")
print("This is the ATM Menu")
input("Press Enter to continue...")

balance = round(float(10000.1234), 2)

def get_valid_deposit():
    while True:
        try:
            d = float(input("Enter the amount you would like to deposit: "))
            if d == 0:
                print("You have not entered a deposit.")
                continue
            elif d < 0:
                print("Error! Amount cannot be negative.")
                continue
            return d
        except ValueError:
            print("Error! Invalid charaters. Enter numbers only.")

def get_valid_withdrawal():
    while True:
        try:
            w = float(input("Enter the amount you would like to withdraw: "))
            if w == 0:
                print("You have not entered a withdrawal.")
                continue
            elif w < 0:
                print("Error! Amount cannot be negative.")
                continue
            elif w > balance:
                print(f"You do not have sufficient funds to withdraw Kshs.{w:.2f}.")
                continue
            return w
        except ValueError:
            print("Error! Invalid characters. Enter numbers only.")

def get_balance(new_balance):
    if balance > new_balance:
        bm = new_balance
        return bm
    elif balance < new_balance:
        bl = new_balance
        return bl

while True:
    try:
        print("-----ATM MENU-----\n")
        print("1. Check Account Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n")
        choice = int(input("Choose what action you would like to perform: "))
        if choice == 1:
            print(f"Your Account Balance is Kshs.{balance}")
            continue
        elif choice == 2:
            deposit = get_valid_deposit()
            new_balance = balance + deposit
            balance = get_balance(new_balance)
            print(f"\nYou have deposited Kshs.{deposit:.2f}\nYour balance is now Kshs.{balance:.2f}")
            continue
        elif choice == 3:
            withdrawal = get_valid_withdrawal()
            new_balance = balance - withdrawal
            balance = get_balance(new_balance)
            print(f"You have withdrawn Kshs.{withdrawal:.2f}\nYour balance is now Kshs.{balance:.2f}")
            continue
        elif choice == 4:
            print("Exiting the menu. Buh byyeeee!")
            break
    except ValueError:
        print("Please pick a choice from 1 to 4!")