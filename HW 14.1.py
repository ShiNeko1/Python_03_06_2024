class CustomError(Exception):
    """Class for custom errors"""

    def __init__(self, message, code=None):
        self.message = message
        self.code = code

    def __str__(self):
        if self.code:
            return f"[Error code {self.code}: {self.message}]"



class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Human):
    students = []

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        Student.students.append(self)

    def __str__(self):
        return super().__str__() + f" {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise CustomError("There are already ten students in the group.", code=400)
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"
        return f'Number: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 25, 'John', 'Johnson', 'AN143')
st4 = Student('Female', 23, 'Kate', 'Moore', 'AN150')
st5 = Student('Female', 32, 'Jane', 'Brown', 'AN140')
st6 = Student('Male', 33, 'Sherlock', 'Homes', 'AN152')
st7 = Student('Male', 27, 'John', 'Watson', 'AN146')
st8 = Student('Female', 30, 'Harrison', 'Smith', 'AN147')
st9 = Student('Male', 25, 'Harry', 'Potter', 'AN156')
st10 = Student('Female', 35, 'Kate', 'Middleton', 'AN157')
st11 = Student('Male', 40, 'Terry', 'Pratchett', 'AN158')

gr = Group('PD1')

for student in Student.students:
    try:
        gr.add_student(student)
    except CustomError as err:
        print(err)
        break

print(gr)

# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only nine students
#
# gr.delete_student('Taylor')  # No error!
