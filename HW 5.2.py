from decimal import Decimal
from time import sleep

math_operators = ('+', '-', '*', '/', 'add', 'sub', 'mul', 'div')
continue_variant = ("y", "yes", "+", "1", "true", "n", "no", "-", "0", "false")

continue_calc = "y"

while continue_calc in continue_variant[0:5]:
    first_number = input("Input first number: ")

    while True:
        try:
            float(first_number)
            break
        except ValueError:
            print("INVALID number! Letters and symbols (except a dot and -) are not accepted.")
            first_number = input("Input first number: ")

    input_math_operator = input("Input operator (+, -, *, /, add, sub, mul, div): ").lower()

    while input_math_operator not in math_operators:
        print("INVALID math operator! Choose from +, -, *, /, add, sub, mul, div.")
        input_math_operator = input("Input math operator: ")

    second_number = input("Input second number: ")

    while True:
        try:
            float(second_number)
            break
        except ValueError:
            print("INVALID number! Letters and symbols (except a dot and -) are not accepted.")
            second_number = input("Input second number: ")

    first_number = Decimal(first_number)
    second_number = Decimal(second_number)
    result_output_str = "Don't you dare to divide by 0 again. >:("

    if input_math_operator in math_operators[::4]:
        result_number = first_number + second_number
        result_output_str = f"The result of {first_number} adding {second_number} equals {result_number}"
    elif input_math_operator in math_operators[1::4]:
        result_number = first_number - second_number
        result_output_str = f"The result of {first_number} subtracting {second_number} equals {result_number}"
    elif input_math_operator in math_operators[2::4]:
        result_number = first_number * second_number
        result_output_str = f"The result of {first_number} multiplied by {second_number} equals {result_number}"
    else:
        if second_number == 0:
            print("UNAUTHORIZED action detected! Division by 0 is not allowed! We are calling the police. >:(")
            sleep(4)
            print("Hey!")
            sleep(1)
            print("DO NOT even try to run to the INFINITY!")
            sleep(2)
            print("We")
            sleep(0.5)
            print("will")
            sleep(0.5)
            print("get you there")
            sleep(0.5)
            print("TOO!")
            sleep(1)
            print("Guys, catch him!")
        else:
            result_number = first_number / second_number
            result_output_str = f"The result of {first_number} divided by {second_number} equals {result_number}"

    print(result_output_str)

    continue_calc = input("Continue? y/n: ").lower()

    while continue_calc not in continue_variant:
        continue_calc = input("I don't understand. Do you want to continue? y/n: ").lower()

else:
    print("END")
