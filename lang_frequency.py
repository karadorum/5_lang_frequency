from collections import Counter
import re
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        text = file.read()
        return text


def get_all_words(text):
    word_list = re.findall("([a-zA-Zа-яА-ЯёЁ']+)", text.lower())
    newlist = []
    for word in word_list:
        newlist.append(word)

    frequency_dict = Counter(newlist)
    return frequency_dict


def get_most_frequent_words(word_dict, words_number):
    most_common = word_dict.most_common(words_number)
    return most_common


if __name__ == '__main__':
    try:
        file_data = load_data(sys.argv[1])
    except FileNotFoundError:
        print('file not found')
    except IndexError:
        print('name of file argument is empty')

    words_number = 10
    most_frequent_words = get_most_frequent_words(get_all_words(file_data), words_number)
    print('Самые частые слова в тексте:')
    for word in most_frequent_words:
        print(word[0], '-', word[1])
