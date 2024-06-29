def say_hi(name, age):
    if not name:
        res = "Error. Name string is empty."
    elif (type(name) is not str or
            type(age) is not int
            or age <= 0):
        res = "Error. Wrong arguments."
    else:
        res = f"Hi. My name is {name.title()} and I'm {age} years old"

    return res


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
