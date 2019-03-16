import unittest
from problem_1 import get_multiplies_of_3_and_5


class MyTestCase(unittest.TestCase):
    def test_basic(self):
        result = 23
        number = 10
        self.assertEqual(result, get_multiplies_of_3_and_5(number))

    def test_1000(self):
        result = 23
        number = 10
        self.assertEqual(result, get_multiplies_of_3_and_5(number))

if __name__ == '__main__':
    unittest.main()
