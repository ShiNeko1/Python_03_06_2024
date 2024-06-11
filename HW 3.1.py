from decimal import Decimal

math_operators = ('+', '-', '*', '/', 'add', 'sub', 'mul', 'div')

first_number = input("Input first number: ")
second_number = input("Input second number: ")
input_math_operator = input("Input operator (+, -, *, /, add, sub, mul, div): ")


if input_math_operator not in math_operators:
    print("Invalid math operator was entered")
    exit()

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