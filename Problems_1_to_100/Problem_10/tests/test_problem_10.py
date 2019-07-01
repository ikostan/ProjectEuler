#!/usr/bin/python


import unittest
import os
from Problems_1_to_100.Problem_10 import is_prime
from Problems_1_to_100.Problem_10 import primes_generator
from Problems_1_to_100.Problem_10 import get_sum


class MyTestCase(unittest.TestCase):

    print("Running unit tests from: " + os.path.basename(__file__) + "\n")

    def test_2000000(self):
        limit = 2000000
        expected = 142913828922
        self.assertEqual(expected, get_sum(limit))

    def test_basic(self):
        limit = 10
        expected = [2, 3, 5, 7]
        self.assertEqual(sum(expected), sum(primes_generator(limit)))

    def test_primes_generator(self):
        limit = 30
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertListEqual(expected, primes_generator(limit))

    def test_is_prime_positive(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in primes:
            self.assertEqual(True, is_prime(i))

    def test_is_prime_negative(self):
        primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 20, 21, 22, 24, 25, 26, 27, 28, 30]
        for i in primes:
            self.assertEqual(False, is_prime(i))


if __name__ == '__main__':
    unittest.main()
