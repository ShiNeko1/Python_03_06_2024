class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise ValueError("There are already ten students in the group.")
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