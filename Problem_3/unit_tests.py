import unittest
from problem_3 import get_largest_prime


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        number = 13195
        primes = [5, 7, 13, 29]
        max_prime = max(primes)
        self.assertEqual(max_prime, get_largest_prime(number))


if __name__ == '__main__':
    unittest.main()
