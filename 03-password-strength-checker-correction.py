print("WELCOME TO THE PASSWORD STRENGTH CHECKER!")
input("Press Enter to continue...")

# ---------------------- CHECKING FUNCTIONS ----------------------

def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False


def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def check_specialchar(password):
    special_chars = ["#", "_", "@", "!"]

    for char in password:
        if char in special_chars:
            return True
    return False


# ---------------------- MAIN PROGRAM ----------------------

while True:

    input("\nPress Enter to view the password requirements...")

    print("\nYour password must contain:")
    print("1. At least 8 characters")
    print("2. At least one uppercase letter")
    print("3. At least one lowercase letter")
    print("4. At least one number")
    print("5. At least one special character (#, _, @, !)")

    password = input("\nEnter your password: ")

    # Keep track of missing requirements
    missing = []

    if len(password) < 8:
        missing.append("At least 8 characters")

    if not check_upper(password):
        missing.append("One uppercase letter")

    if not check_lower(password):
        missing.append("One lowercase letter")

    if not check_digit(password):
        missing.append("One number")

    if not check_specialchar(password):
        missing.append("One special character (#, _, @, !)")

    # ---------------- Strength ----------------

    if len(missing) == 0:

        if len(password) >= 12:
            print("\n✅ Password Strength: STRONG")
        else:
            print("\n✅ Password Strength: MODERATE")
            print("Tip: A longer password (12+ characters) is even stronger.")

        break

    elif len(missing) <= 2:
        print("\n⚠ Password Strength: MODERATE")
    else:
        print("\n❌ Password Strength: WEAK")

    print("\nMissing Requirements:")

    for item in missing:
        print(f"- {item}")

    print("\nPlease try again.\n")