#!/usr/bin/python


from utils.utils import print_time_log, get_full_path, calc_triangle_number
import time
import string

alphabet = list(string.ascii_uppercase)


def find_max_numeric_value(words: list):
    '''
    calc numeric value per each word and return the max
    :param words:
    :return:
    '''

    max_value = {'word': '', 'digit': 0}

    for word in words:
        if calc_word_number(word) > max_value['digit']:
            max_value['word'] = word
            max_value['digit'] = calc_word_number(word)

    return max_value


def calc_word_number(word: str):
    '''
    Returns word's numerical value by converting each letter in a word
    to a number corresponding to its alphabetical position and adding these values
    :param word:
    :return:
    '''

    result = 0
    for char in word:
        result += alphabet.index(char) + 1

    return result


def words_reader(file_folder: str, file_name: str):
    '''
    Reads file and returns all words as a list
    :param file_folder:
    :param file_name:
    :return:
    '''

    results = list()
    path = get_full_path(file_folder, file_name)
    with open(path, 'r') as reader:
        for line in reader:
            results += [l.strip('"') for l in line.split(',')]
    return results


def generate_triangle_numbers(words: list):
    '''
    Generates set of possible triangle numbers
    up to max possible value based on the words list
    :param words:
    :return:
    '''

    triangle_numbers = set()
    n = 1
    max_word = find_max_numeric_value(words)['digit']

    while True:
        triangle_numbers.add(calc_triangle_number(n))
        n += 1
        if max(triangle_numbers) > max_word:
            break

    print(triangle_numbers)
    return triangle_numbers


def is_triangle(word: str, triangle_numbers: set):
    '''
    Check if word's value is triangle number
    :param word:
    :param triangle_numbers:
    :return:
    '''

    if calc_word_number(word) in triangle_numbers:
        return True
    return False


def main(words: list):
    '''
    Using words.txt (right click and 'Save Link/Target As...'),
    a 16K text file containing nearly two-thousand common English words,
    how many are triangle words?
    :param words:
    :return:
    '''

    start_time = time.time()
    how_many_triangle_words = 0
    triangle_numbers = generate_triangle_numbers(words)

    for word in words:
        if is_triangle(word, triangle_numbers):
            how_many_triangle_words += 1

    print_time_log(start_time, how_many_triangle_words)
    return how_many_triangle_words
