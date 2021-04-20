import re


def multiple_replace(string_to_parse, replace_values):
    for i in replace_values:
        string_to_parse = string_to_parse.replace(i, '')
    return string_to_parse


def create_words(text):
    replace_values = ['.', ',', '!', '?', ':', ';', '-']
    return list(filter(lambda x: len(x) > 3,
                       [x.strip() for x in multiple_replace(text, replace_values).split(' ')]))


def create_sentences(text):
    return list(filter(lambda x: len(x) > 10,
                       [x.strip() for x in re.split('\.|\?|!|\n', text)]))
