import re


def multiple_replace(string_to_parse):
    replace_values = ['.', ',', '!', '?', ':', ';', '-', '(', ')', '*', '\n', '[', ']', '{', '}']
    for i in replace_values:
        string_to_parse = string_to_parse.replace(i, ' ')
    return string_to_parse


def create_words(text, topic, cur_dict):
    cur_dict[topic] = list(filter(lambda x: len(x) > 3, re.findall(r'[\w]+', text)))


def create_sentences(text, topic, cur_dict):
    cur_dict[topic] = list(filter(lambda x: len(x) > 10,
                                              [x.strip() for x in re.split('\.|\?|!|\n', text)]))


def create_text(text, topic, cur_dict):
    cur_dict[topic] = [text.replace('\n', ' ')]


def delete_key(topic,  cur_dict):
    del(cur_dict[topic])

