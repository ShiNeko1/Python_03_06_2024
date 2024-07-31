from math import gcd


class CustomError(Exception):
    """Class for custom errors"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"[{self.message}]"


class Fraction:
    """Class of fractions"""

    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise CustomError("ValueError: numerator and denominator must be int.")

        self.a = a
        self.b = b

    @staticmethod
    def fraction_reduction(a, b):
        """To reduce a fraction"""
        greater_cmn_div = gcd(a, b)

        if greater_cmn_div > 1:
            a = int(a / greater_cmn_div)
            b = int(b / greater_cmn_div)
            return a, b
        else:
            return a, b

    # def common_denominator(self, other): # not used right now
    #     """To find a common denominator of two fractions"""
    #     if isinstance(other, Fraction):
    #         greater_cmn_div = gcd(self.b, other.b)
    #         return self.b * other.b / greater_cmn_div

    def find_multiplier(self, b):
        """To find a multiplier for a numerator when leading two fractions to a common denominator"""
        greater_cmn_div = gcd(self.b, b)
        return int(self.b / greater_cmn_div)

    def __mul__(self, other):
        """Method to multiply two fractions"""
        if isinstance(other, int):
            other = self.conv_int_to_fraction(other)

        if not isinstance(other, Fraction):
            raise CustomError("ClassError: fraction can't be multiplied by something other than Fraction or int")

        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        """Method to add two fractions"""
        if isinstance(other, int):
            other = self.conv_int_to_fraction(other)

        if not isinstance(other, Fraction):
            raise CustomError("ClassError: fraction can't be added to something other than Fraction or int")

        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        # new_a, new_b = self.fraction_reduction(new_a, new_b)
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        """Method to subtract two fractions"""
        return self + other * (-1)

    def __eq__(self, other):
        """Boolean to check whether two fractions are equal"""
        if isinstance(other, int):
            other = self.conv_int_to_fraction(other)

        if isinstance(other, Fraction):
            a_self, b_self = self.fraction_reduction(self.a, self.b)
            a_other, b_other = self.fraction_reduction(other.a, other.b)
            return all((a_self == a_other, b_self == b_other))

        raise CustomError("ClassError: fraction can't be compared to something other than Fraction or int")

    def __gt__(self, other):
        """Boolean to check whether one fraction is greather than the other"""
        if isinstance(other, Fraction):
            a_self = self.a * other.b
            a_other = other.a * self.b
            return a_self > a_other

    # def __lt__(self, other): # No need to define
    #     pass

    def conv_to_proper(self):
        """Method to convert the fraction to class proper fraction if possible"""
        if not ProperFraction.can_be_proper_frac(self.a, self.b):
            raise CustomError("ClassError: the numerator can't be greater than denominator for a proper fraction.")

        return ProperFraction(self.a, self.b)

    @staticmethod
    def conv_int_to_fraction(num):
        """To convert int into fraction"""
        if isinstance(num, int):
            return Fraction(num, 1)

    def __str__(self):
        """To describe the class instance"""
        return f"Fraction: {self.a}, {self.b}"


class ProperFraction(Fraction):
    """Class of proper fractions"""

    def __init__(self, a, b):
        """Method to initialize class instance"""
        a, b = super().fraction_reduction(a, b)
        if self.can_be_proper_frac(a, b):
            super().__init__(a, b)
        else:
            raise CustomError("ClassError: the numerator can't be greater than denominator for a proper fraction.")

    @staticmethod
    def can_be_proper_frac(a, b):
        """Method to check whether the fraction is proper with given parameters"""
        return a < b

    def __mul__(self, other):
        """Method to multiply two proper fractions.The result is not always a proper fraction."""
        frac = super().__mul__(other)
        if self.can_be_proper_frac(frac.a, frac.b):
            new_a, new_b = super().fraction_reduction(frac.a, frac.b)
            return ProperFraction(new_a, new_b)
        else:
            new_a, new_b = super().fraction_reduction(frac.a, frac.b)
            return Fraction(new_a, new_b)

    def __add__(self, other):
        """Method to add two proper fractions.The result is not always a proper fraction."""
        frac = super().__add__(other)
        if self.can_be_proper_frac(frac.a, frac.b):
            new_a, new_b = super().fraction_reduction(frac.a, frac.b)
            return ProperFraction(new_a, new_b)
        else:
            return frac

    def __sub__(self, other):
        """Method to subtract two proper fractions.The result is not always a proper fraction."""
        return self + other * (-1)

    def conv_to_class_frac(self):
        """Method to convert the proper fraction to class fraction"""
        return Fraction(self.a, self.b)

    def __str__(self):
        """To describe the class instance"""
        tmp = super().__str__()
        return "Proper " + tmp.lower()


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

pf_a = ProperFraction(3, 13)
pf_b = ProperFraction(1, 2)
pf_c = pf_a + pf_b
assert str(pf_c) == 'Proper fraction: 19, 26'
pf_d = pf_b * pf_a
assert str(pf_d) == 'Proper fraction: 3, 26'
pf_e = pf_a - pf_b
assert str(pf_e) == 'Proper fraction: -7, 26'

pf_f = ProperFraction(10, 13)
f_1 = pf_b + pf_f
assert str(f_1) == 'Fraction: 33, 26'
f_2 = pf_b * pf_f
assert str(f_2) == 'Proper fraction: 5, 13'

f_3 = Fraction(3, 1)
f_4 = pf_b + f_3
assert str(f_4) == 'Fraction: 7, 2'
f_5 = pf_b * f_3
assert str(f_5) == 'Fraction: 3, 2'

c = pf_f.conv_to_class_frac()
print(c)

d = f_a.conv_to_proper()
print(d)
