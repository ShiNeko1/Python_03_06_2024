import string

wanted_range = input('Input wanted range of the letters (in "chr-CHR" form): ').lstrip(string.punctuation + " ")

while True:
    if len(wanted_range) < 3:
        wanted_range = input('Not enough data. Input wanted range of the letters (in "chr-CHR" form): ')
    elif (wanted_range[0] not in string.ascii_letters
          or wanted_range[2] not in string.ascii_letters
          or wanted_range[1] != "-"):
        wanted_range = input('Incorrect input. Please, use "chr-CHR" form: ')
    else:
        break

letter_index_1 = string.ascii_letters.find(wanted_range[0])
letter_index_2 = string.ascii_letters.find(wanted_range[2])

letter_index_1, letter_index_2 = min(letter_index_1, letter_index_2), max(letter_index_1, letter_index_2)

print("Here is your range: ", string.ascii_letters[letter_index_1:letter_index_2 + 1])
