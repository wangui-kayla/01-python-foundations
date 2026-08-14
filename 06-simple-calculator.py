import time

def get_details():
    list_operators = ("+", "-", "*", "/")
    try:
        first_number = round(float(input("Enter the First Number: ")), 2)
        operator = input("Enter the Operator between (+  -  *  /): ")
        if operator not in list_operators:
            raise ValueError("Error! Choose between the listed operators:\n+ ~ Addition\n- ~ Subtraction\n* ~ Multiplication\n/ ~ Division")
        second_number = round(float(input("Enter the Second Number: ")), 2)

    except ValueError as err:
        print(f"Error! {err}")

    return first_number, operator, second_number

def calculations(first_number, operator, second_number):
    while True:
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

        except ZeroDivisionError as err:
            print(f"Error! {err}")

        return result

calculating = True
while calculating:
    print("Welcome to the Calculator!")
    time.sleep(1)

    first_num, op, second_num = get_details()

    answer = calculations(first_num, op, second_num)

    print("Result...")
    time.sleep(1)
    print(f"{first_num} {op} {second_num} = {answer}")

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


    



