from human import Human


class Student(Human):
    students = []

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        Student.students.append(self)

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        elif isinstance(other, str):
            return str(self) == other

    def __str__(self):
        return super().__str__() + f" {self.record_book}"

    def __hash__(self):
        return hash(str(self))

