import codecs


def text_cleaner(text, symb1, symb2):
    begin = text.find(symb1)
    end = text.find(symb2)

    while begin != -1:
        text = text.replace(text[begin:end + 1], "")
        begin += text[begin:].find(symb1)
        end = text[begin:].find(symb2) + begin

    return text


def delete_empty_lines(text):
    return "\n".join([line.strip() for line in text.splitlines() if line.strip()])


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        cleaned_text = text_cleaner(html, "<", ">")
        cleaned_text = delete_empty_lines(cleaned_text)

        with codecs.open(result_file, 'w', 'utf-8') as result:
            result.write(cleaned_text)


delete_html_tags("draft.html")
