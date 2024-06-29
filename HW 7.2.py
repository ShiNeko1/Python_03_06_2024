def string_checker(text):
    return not text or not isinstance(text, str)


def correct_sentence(text):
    if string_checker(text):
        return "Error"

    sentences = text.split(". ")
    res = []
    for sent in sentences:
        if not sent.endswith("."):
            res.append(sent[0].upper() + sent[1:] + ".")
        else:
            res.append(sent[0].upper() + sent[1:])

    res = " ".join(res)

    return res


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
