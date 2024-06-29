def string_checker(text):
    return not text or not isinstance(text, str)


def second_index(text, some_str):
    if string_checker(text) or string_checker(some_str):
        return "Error"

    first_index = text.find(some_str)
    result = first_index + 1 + text[first_index + 1:].find(some_str)

    return None if result == 0 else result


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
