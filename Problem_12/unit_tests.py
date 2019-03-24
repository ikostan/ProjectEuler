import unittest
from problem_12 import triangle_number_generator


class MyTestCase(unittest.TestCase):
    def test_triangle_number_generator(self):
        counter = 7
        expected = 28
        self.assertEqual(expected, triangle_number_generator(counter)['total'])


if __name__ == '__main__':
    unittest.main()
