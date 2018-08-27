from collections import Counter
import re
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        text = file.read()
        return text


def get_most_frequent_words(text):
    r = re.compile("([a-zA-Zа-яА-ЯёЁ']+)")
    text_data = r.findall(text)

    newlist = []
    for word in text_data:
        newlist.append(word.lower())

    frequency_dict = Counter(newlist)
    return frequency_dict


def print_result(word_dict):
    most_common = word_dict.most_common(10)
    for pair in most_common:
        print(pair[0], '-', pair[1])


if __name__ == '__main__':
    try:
        file_data = load_data(sys.argv[1])
    except FileNotFoundError:
        print('file not found')
    except IndexError:
        print('name of file argument is empty')

    print('Самые частые слова в тексте:')
    print_result(get_most_frequent_words(file_data))
