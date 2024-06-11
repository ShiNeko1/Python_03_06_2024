list_one = [1, 2, 3, 4, 5, 6]
list_two = [1, 2, 3]
list_three = [1, 2, 3, 4, 5]
list_four = [1]
list_five = []

work_list = list_one
# work_list = list_two
# work_list = list_three
# work_list = list_four
# ork_list = list_five

list_length = len(work_list)
result_list = []

if (not work_list):
    result_list = [work_list, []]
elif list_length % 2 == 0:
    list_breaker = list_length // 2

    result_list = [work_list[0:list_breaker], work_list[list_breaker:]]
else:
    list_breaker = 1 + list_length // 2

    result_list = [work_list[0:list_breaker], work_list[list_breaker:]]

print("RESULT:", result_list)
