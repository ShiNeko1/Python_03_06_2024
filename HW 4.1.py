list_1 = [0, 0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
list_5 = []

work_list = list_1
# work_list = list_2
# work_list = list_3
# work_list = list_4
# work_list = list_5

print("Original list: ", work_list)


#### First variant ####

# number_of_zeros = work_list.count(0)
#
# new_list = []
#
# for element in work_list:
#     if element != 0:
#         new_list.append(element)
# else:
#     new_list.extend([0] * number_of_zeros)

# print("Result: ", new_list)

#### END of the first variant ####


#### Second variant ####

# list_len = len(work_list)
#
# for index in range(-1, -list_len-1, -1):
#     if work_list[index] == 0:
#         work_list.pop(index)
#         work_list.append(0)
#
# print("Result: ", work_list)

#### END of the second variant ####


#### Third variant ####

# number_of_zeros = work_list.count(0)
#
# for iteration in range(0, number_of_zeros):
#     work_list.remove(0)
#     work_list.append(0)
#
# print("Result: ", work_list)

#### END of the third variant ####


#### Fourth variant ####

# zero_counter = 0
#
# while 0 in work_list:
#     work_list.remove(0)
#     zero_counter += 1
# else:
#     work_list.extend([0] * zero_counter)
#
# print("Result: ", work_list)

#### END of the fourth variant ####


#### Fifth variant ####
def sort_zeros(list_element):
    return list_element == 0


work_list.sort(key=sort_zeros)

print("Result: ", work_list)

#### END of the fifth variant ####
