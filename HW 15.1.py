class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"[{self.message}]"


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise CustomError("ClassError: rectangle can't be compared to non-rectangle.")

        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise CustomError("ClassError: rectangle can't be added to non-rectangle.")

        new_area = self.get_square() + other.get_square()
        new_width = self.get_new_side(self.width, other.width)
        return Rectangle(new_width, new_area / new_width)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            raise CustomError("ClassError: rectangle can't be multiplied by something other than int or float.")

        return Rectangle(self.width, self.height * n)

    @staticmethod
    def get_new_side(side_one, side_two):
        new_side = side_one + side_two
        return new_side

    def __str__(self):
        return f"Rectangle: width {self.width}, height {self.height}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

r5 = Rectangle(0.5, 0.2)
r6 = r5 + r2
assert r6.get_square() == 18.1, 'Test6'
