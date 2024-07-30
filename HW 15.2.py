from math import gcd

class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"[{self.message}]"

class Fraction:
    def __init__(self, a, b):
        self.a, self.b = self.conv_to_proper_fraction(a, b)

    @staticmethod
    def conv_to_proper_fraction(a, b):
        greater_cmn_div = gcd(a, b)
        # if a >= b:
        #     raise CustomError("ClassError: the numenator is greater than denominator.")
        if greater_cmn_div > 1:
            a = int(a / greater_cmn_div)
            b = int(b / greater_cmn_div)
            return a, b
        else:
            return a, b


    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        elif isinstance(other, int):
            return Fraction(self.a*other, self.b)

        raise CustomError("ClassError: fraction can't be multiplied by something other than Fraction or int")
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
            new_a, new_b = self.conv_to_proper_fraction(new_a, new_b)
            return Fraction(new_a, new_b)
        elif isinstance(other, int):
            new_a = self.a + self.b * other
            new_a, new_b = self.conv_to_proper_fraction(new_a, self.b)
            return Fraction(new_a, new_b)

        raise CustomError("ClassError: fraction can't be added to something other than Fraction or int")

    def __sub__(self, other):
        return self + other * (-1)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return all((self.a == other.a, self.b == other.b))

        raise CustomError("ClassError: fraction can't be compared to something other than Fraction or int")


    def __gt__(self, other):
        if isinstance(other, Fraction):


    def __lt__(self, other):
        return other > self

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')