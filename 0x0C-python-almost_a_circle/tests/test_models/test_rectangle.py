#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(5, 10, 2, 3, 4)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 4)

    def test_width_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

    def test_height_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.height, 10)
        rectangle.height = 20
        self.assertEqual(rectangle.height, 20)

    def test_x_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.x, 0)
        rectangle.x = 3
        self.assertEqual(rectangle.x, 3)

    def test_y_property(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.y, 0)
        rectangle.y = 4
        self.assertEqual(rectangle.y, 4)

    def test_to_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 3, 4)
        expected_dict = {'x': 2, 'y': 3, 'id': 4, 'height': 10, 'width': 5}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

if __name__ == '__main__':
    unittest.main()

