from group import Group
from student import Student

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
    except ValueError as err:
        print(err)
        break
print(gr)


assert gr.find_student('Jobs') == st1, 'Test1'   # 'Steve Jobs'
assert gr.find_student('Jobs2') is None, 'Test2'
assert gr.find_student('Johnson') == "John Johnson AN143", 'Test3'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only nine students

gr.delete_student('Taylor')  # No error!

