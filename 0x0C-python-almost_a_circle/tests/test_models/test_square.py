#!/usr/bin/python3
"""Module for Suare unit tests."""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_size_property(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 4)
        expected_dict = {'id': 4, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_update(self):
        square = Square(5, 2, 3, 4)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.x, 40)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.y, 3)

    def test_str(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 5")

if __name__ == '__main__':
    unittest.main()

