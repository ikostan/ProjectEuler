#!/usr/bin/python


def generate_terms(start: int, end: int):

    terms = set()

    for n in range(start, end + 1):
        for power in range(start, end + 1):
            terms.add(n ** power)

    return terms
