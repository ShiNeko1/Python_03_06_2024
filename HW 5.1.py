import keyword
import string

variable_name = input("Input a variable name: ")

if not variable_name:
    result = False
    print(result)
    exit()

punct_checker = False
capital_checker = False

for punct_counter in string.punctuation:
    if punct_counter == "_":
        continue
    elif variable_name.find(punct_counter) != -1:
        punct_checker = True
        break

for capital_counter in range(65, 91):
    if variable_name.find(chr(capital_counter)) != -1:
        capital_checker = True
        break

#### First Variant ####

if punct_checker:
    result = False
elif capital_checker:
    result = False
elif variable_name in keyword.kwlist:
    result = False
elif variable_name.count("_") == len(variable_name) and len(variable_name) > 1:
    result = False
elif variable_name[0].isnumeric():
    result = False
elif variable_name.find(" ") != -1:
    result = False
else:
    result = True

#### END of the first variant ####


#### Second Variant ####

# if not variable_name.isidentifier():
#     result = False
# elif variable_name in keyword.kwlist:
#     result = False
# elif capital_checker:
#     result = False
# elif variable_name.count("_") == len(variable_name) and len(variable_name) > 1:
#     result = False
# else:
#     result = True

#### END of the second variant ####

print(result)
