def common_elements():
    set_mul_of_3 = {num for num in range(0, 100, 3)}
    set_mul_of_5 = {num for num in range(0, 100, 5)}
    result = set_mul_of_3.intersection(set_mul_of_5)
    return result


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test'
print('OK')