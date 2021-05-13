import re
from modules import dictionary


def multiple_replace(string_to_parse):
    replace_values = ['.', ',', '!', '?', ':', ';', '-']
    for i in replace_values:
        string_to_parse = string_to_parse.replace(i, ' ')
    return string_to_parse


def create_words(text, topic):
    dictionary.sentences[topic] = list(filter(lambda x: len(x) > 3,
                                              [x.strip() for x in multiple_replace(text).split(' ')]))


def create_sentences(text, topic):
    dictionary.sentences[topic] = list(filter(lambda x: len(x) > 10,
                                              [x.strip() for x in re.split('\.|\?|!|\n', text)]))


def create_text(text, topic):
    dictionary.sentences[topic] = [text]


def delete_key(topic):
    del(dictionary.sentences[topic])

