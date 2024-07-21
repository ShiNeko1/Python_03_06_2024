import codecs


def gen_remove_elm(text: str, symb1: str, symb2: str) -> list:
    """This generator finds all substrings in the text which are between two symbols"""

    begin = text.find(symb1)
    end = text.find(symb2, begin+1)

    while begin != -1:
        yield text[begin:end+1]
        begin = text.find(symb1, end+1)
        end = text.find(symb2, begin+1)

    return


def text_cleaner(text: str, to_remove: list) -> str:
    """This function removes all the substrings form the list in a text"""

    for elm in to_remove:
        text = text.replace(elm, "")
    return text


def delete_empty_lines(text: str) -> str:
    """Removes all empty lines in a text"""
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """This function deletes tags in a text and writes the cleared text into a new file"""

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        cleaned_text = text_cleaner(html, list(gen_remove_elm(html, "<", ">")))
        cleaned_text = delete_empty_lines(cleaned_text)

        with codecs.open(result_file, 'w', 'utf-8') as result:
            result.write(cleaned_text)


delete_html_tags("draft.html")
