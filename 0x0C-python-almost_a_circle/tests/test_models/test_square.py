import unittest
from models.square import Square

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
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)
        self.assertEqual(square.size, 40)

    def test_str(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 5")

if __name__ == '__main__':
    unittest.main()

