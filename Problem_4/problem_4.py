#!/usr/bin/python


import time


def is_palindrome(number):
    word = str(number)

    if len(word) % 2 != 0:
        return False

    if word == word[::-1]:
        return True

    return False

