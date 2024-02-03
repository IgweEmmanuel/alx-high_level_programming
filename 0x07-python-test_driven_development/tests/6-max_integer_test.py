#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_normal_case(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5)

    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_negative_numbers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1)

    def test_max_integer_duplicate_numbers(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_max_integer_single_element(self):
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_mixed_numbers(self):
        result = max_integer([5, -2, 0, 10, -8])
        self.assertEqual(result, 10)

    def test_max_integer_float_numbers(self):
        result = max_integer([1.5, 3.7, 2.1, 4.8])
        self.assertEqual(result, 4.8)


if __name__ == '__main__':
    unittest.main()

