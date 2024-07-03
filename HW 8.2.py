def is_palindrome(text):
    import string

    only_letters = text.lower()

    for punct in (string.punctuation + " "):
        only_letters = only_letters.replace(punct, "")

    if only_letters == only_letters[::-1]:
        result = True
    else:
        result = False

    return result


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")