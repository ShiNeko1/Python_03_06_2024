import random

#### First variant ####

# random_list_len = random.randint(3, 10)
# random_list = []
#
# for index in range(random_list_len):
#     random_list.append(random.randint(-9, 9))

#### END of the first variant ####


#### Second variant ####

random_list = random.sample(range(-9, 9), random.randint(3, 10))

#### END of the second variant ####

print(random_list)

new_list = [random_list[0], random_list[2], random_list[-2]]

print(new_list)