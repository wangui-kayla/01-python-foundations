import time

def get_details():
    list_operators = ("+", "-", "*", "/")
    while True:
        try:
            first_number = float(input("Enter the First Number: "))
            operator = input("Enter the Operator between (+  -  *  /): ")
            if operator not in list_operators:
                raise ValueError("Error! Choose between the listed operators:\n+ ~ Addition\n- ~ Subtraction\n* ~ Multiplication\n/ ~ Division")
            second_number = float(input("Enter the Second Number: "))

            return first_number, operator, second_number

        except ValueError as err:
            print(f"{err}")

def calculations(first_number, operator, second_number):
    try:
        if operator == "+":
            print("Calculating...")
            time.sleep(1)
            result = first_number + second_number
        elif operator == "-":
            print("Calculating...")
            time.sleep(1)
            result = first_number - second_number
        elif operator == "*":
            print("Calculating...")
            time.sleep(1)
            result = first_number * second_number
        elif operator == "/":
            print("Calculating...")
            time.sleep(1)
            result = first_number / second_number

        return result

    except ZeroDivisionError as err:
        print(f"{err}")
        return None

calculating = True
while calculating:
    print("Welcome to the Calculator!")
    time.sleep(1)

    while True:
        first_num, op, second_num = get_details()

        answer = calculations(first_num, op, second_num)

        if answer is None:
            continue
        else:
            break

    print("Result...")
    time.sleep(1)
    print(f"{first_num:.2f} {op} {second_num:.2f} = {answer:.2f}")

    while True:
        retry = input("Would you like to calculate again? (Y/N): ").upper()
        if retry == "Y":
            print("Going back to calculator...")
            time.sleep(1.5)
            break
        elif retry == "N":
            print("Exiting calculator... Buh Byeeeee!")
            time.sleep(1.5)
            calculating = False
            break
        else:
            print("Type a valid answer between Y and N")
            continue