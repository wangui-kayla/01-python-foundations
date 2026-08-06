print("WELCOME TO THE PASSWORD STRENGTH CHECKER!")
input("Continue...")

def check_upper():
    count_upper = 0

    for char in password:
        if char.isupper() == True:
            count_upper += 1
        else:
            pass

    if count_upper != 0:
        return count_upper
    else:
        print("Error! Password must contain at least ONE uppercase letter.")
        return

def check_lower():
    count_lower = 0

    for char in password:
        if char.islower() == True:
            count_lower += 1
        else:
            pass

    if count_lower != 0:
        return count_lower
    else:
        print("Error! Password must contain at least ONE lowercase letter.")
        return

def check_digit():
    count_digit = 0

    for char in password:
        if char.isdigit() == True:
            count_digit += 1
        else:
            pass

    if count_digit != 0:
        return count_digit
    else:
        print("Error! Password must contain at least ONE number (0-9).")
        return

def check_specialchar():
    count_specialchar = 0
    special_chars = ["#", "_", "@", "!"]

    for char in password:
        if special_chars in char:
            count_specialchar += 1
        else:
            pass

    if count_specialchar != 0:
        return count_specialchar
    else:
        print("Error! Password must contain at least ONE special character (#, _, @, !).")
        return

while True:
    input("These are the rules for the password...")
    print("The Password must contain: ")
    print("\n1. At least 8 characters\n2. At least one uppercase letter\n3. At least one lowercase letter\n4. At least one number\n5. At least one special character (#, _, @, !)")
    password = input("Enter your Password: ")

    if len(password) >= 8:
        cu = check_upper()
        cl = check_lower()
        cd = check_digit()
        #cs = check_specialchar()
        if 8 <= len(password) < 10:
            input("Your password may be correct...")
            print("But it is WEAK.")
            print("Enter ten digits or more to make it stronger.")
            continue
        elif len(password) >= 10 and cd <= 2: #cs <= 2
            input("Your password may be correct...")
            print("But it is merely MODERATE.")
            print("Enter more than ten digits and more than two numbers to make it stronger.")
            continue
        elif len(password) > 10:
            input("You have successfully created your password!")
            print("Your password is STRONG.")
            break
    else:
        print("Error! Password must contain at least EIGHT characters.")
        continue
