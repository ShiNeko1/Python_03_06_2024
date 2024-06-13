list_one = [12, 3, 4, 10]
list_two = [1]
list_three = []
list_four = [45, "two", 6, -4, 0, None, 3]

# work_list = list_one
work_list = list_two
# work_list = list_three
# work_list = list_four

result_list = []

if not work_list:
    result_list = work_list
else:
    result_list = [work_list[-1]]
    result_list[1:] = work_list[0:-1]

print("RESULT:", result_list)