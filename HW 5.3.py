import string

input_hashtag = ""
all_punctuation = string.punctuation + " №₴"

while not input_hashtag:
    while not input_hashtag:
        input_hashtag = input("Input a string to make a hashtag: ")

    input_hashtag = input_hashtag.strip(all_punctuation)
    input_hashtag = input_hashtag.title()

    for punct in all_punctuation:
        input_hashtag = input_hashtag.replace(punct, "")

    if not input_hashtag:
        print("You've input only punctuation symbols for a hashtag.")


if len(input_hashtag) > 139:
    input_hashtag = input_hashtag[:139]

input_hashtag = "#" + input_hashtag

print(input_hashtag)

