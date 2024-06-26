import string

input_number = ""

while not input_number.isdigit():
    input_number = input("Input an integer: ").strip(string.punctuation + " ")

number_len = len(input_number)
mul_number = input_number
mul = 1

while number_len > 1:
    for work_digit in mul_number:
        mul *= int(work_digit)

    mul_number = str(mul)
    number_len = len(mul_number)
    mul = 1

print(mul_number)
