list_of_lists = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], [], [1, 5, 5, 1, 6, 5]]

# work_list = list_of_lists[0]
# work_list = list_of_lists[1]
work_list = list_of_lists[2]
# work_list = list_of_lists[3]
# work_list = list_of_lists[4]

if not work_list:
    print(0)
    exit()

#### First Variant ####

# result_sum = 0
# list_len = len(work_list)
#
# for index in range(0, list_len, 2):
#     result_sum += work_list[index]
# else:
#     result_sum *= work_list[-1]

#### END of the first variant ####


#### Second variant ####

list_of_even = work_list[::2]

result_sum = sum(list_of_even) * work_list[-1]

#### END of the second variant ####

print(result_sum)