from decimal import Decimal

math_operators = ('+', '-', '*', '/', 'add', 'sub', 'mul', 'div')

first_number = input("Input first number: ")

while True:
    try:
        float(first_number)
        break
    except ValueError:
        print("INVALID number! Letters and symbols (except a dot and -) are not accepted.")
        first_number = input("Input first number: ")

second_number = input("Input second number: ")

while True:
    try:
        float(second_number)
        break
    except ValueError:
        print("INVALID number! Letters and symbols (except a dot and -) are not accepted.")
        second_number = input("Input second number: ")

input_math_operator = input("Input operator (+, -, *, /, add, sub, mul, div): ")

while input_math_operator not in math_operators:
    print("INVALID math operator! Choose from +, -, *, /, add, sub, mul, div.")
    input_math_operator = input("Input math operator: ")

first_number = Decimal(first_number)
second_number = Decimal(second_number)

if input_math_operator in math_operators[::4]:
    result_number = first_number + second_number
    result_output_str = f"The result of {first_number} adding {second_number} equals {result_number}"
elif input_math_operator in math_operators[1::4]:
    result_number = first_number - second_number
    result_output_str = f"The result of {first_number} subtracting {second_number} equals {result_number}"
elif input_math_operator in math_operators[2::4]:
    result_number = first_number * second_number
    result_output_str = f"The result of {first_number} multiplying {second_number} equals {result_number}"
else:
    result_number = first_number / second_number
    result_output_str = f"The result of {first_number} dividing {second_number} equals {result_number}"

print(result_output_str)
