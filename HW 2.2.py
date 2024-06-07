five_digit_integer = input("Input a five-digit integer: ")
five_digit_integer = abs(int(five_digit_integer))

ten_thousands_of_the_integer = divmod(five_digit_integer, 10000)
thousands_of_the_integer = divmod(ten_thousands_of_the_integer[1], 1000)
hundreds_of_the_integer = divmod(thousands_of_the_integer[1], 100)
decimals_of_the_integer = divmod(hundreds_of_the_integer[1], 10)

inverted_integer = (decimals_of_the_integer[1] * 10000 + decimals_of_the_integer[0] * 1000
                    + hundreds_of_the_integer[0] * 100 + thousands_of_the_integer[0] * 10
                    + ten_thousands_of_the_integer[0])

print("Result: ", inverted_integer)