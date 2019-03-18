#!/usr/bin/python


import time


def is_palindrome(number):
    word = str(number)

    if word == word[::-1]:
        return True

    return False

