four_digit_integer = input("Input a four-digit integer: ")
four_digit_integer = abs(int(four_digit_integer))

#### First version ####
# units_of_the_integer = four_digit_integer % 10
# decimals_of_the_integer = (four_digit_integer % 100 - units_of_the_integer) // 10
# thousands_of_the_integer = four_digit_integer // 1000
# hundreds_of_the_integer = four_digit_integer // 100 - thousands_of_the_integer * 10

#### Second version ####
thousands_of_the_integer = divmod(four_digit_integer, 1000)
hundreds_of_the_integer = divmod(thousands_of_the_integer[1], 100)
decimals_of_the_integer = divmod(hundreds_of_the_integer[1], 10)


print("Result:")
print(thousands_of_the_integer[0])
print(hundreds_of_the_integer[0])
print(decimals_of_the_integer[0])
print(decimals_of_the_integer[1])
