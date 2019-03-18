#!/usr/bin/python


import time


def is_palindrome(number: int):
    # convert a number to string
    word = str(number)
    # reverse string and compare to itself
    if word == word[::-1]:
        return True
    return False


def large_palindrome_generator(start: int, end: int):
    start_time = time.time()
    max_palindrome = 0

    for i in range(start, end + 1):
        for b in range(start, end + 1):
            n = i * b
            if is_palindrome(n):
                if n > max_palindrome:
                    max_palindrome = n
    print("The answer {0} returned in {1} seconds".format(max_palindrome, time.time() - start_time))
    return max_palindrome

