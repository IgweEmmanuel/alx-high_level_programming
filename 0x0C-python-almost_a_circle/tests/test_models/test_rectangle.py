#!/usr/bin/python3
"""Module for Rectangle unit tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io

class TestRectangle(unittest.TestCase):
    """Test the Base class"""

    def setUp(self):
        """Instantiate class"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clear all instances after result"""
        pass

    def test_if_class(self):
        """Is it a class"""
        self.assertEqual(str(Rectangle), 
                        "<class 'models.rectangle.Rectangle'>")

    def test_if_subclass(self):
        """Check if subclass"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_empty_class(self):
        """Tests if the class is empty"""
        with self.assertRaises(TypeError) as e:
            Rectangle.__init__()
        msg = "__init__() missing 3 required positional arguments: 'self', 'width', and 'height'"
        self.assertEqual(str(e.exception), msg)

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

    def test_I_area_no_args(self):
        '''Tests area() method signature.'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() method compuation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(r.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\










          #
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)


    def test_K_str_no_args(self):
        '''Tests __str__() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        r = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(r), s)
        r = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(r), s)
        r = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(r), s)

        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_L_update_no_args(self):
        '''Tests update() method signature.'''
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError) as e:
            Rectangle.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = r.__dict__.copy()
        r.update()
        self.assertEqual(r.__dict__, d)

    def test_L_update_args(self):
        '''Tests update() postional args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(10, 5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(10, 5, 17, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_args_bad(self):
        '''Tests update() positional arg fubars.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        with self.assertRaises(ValueError) as e:
            r.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, -17)
        s = "height must be > 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, -20)
        s = "x must be >= 0"
        self.assertEqual(str(e.exception), s)

        with self.assertRaises(ValueError) as e:
            r.update(10, 5, 17, 20, -25)
        s = "y must be >= 0"
        self.assertEqual(str(e.exception), s)

    def test_L_update_kwargs(self):
        '''Tests update() keyword args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

    def test_L_update_kwargs_2(self):
        '''Tests update() keyword args.'''
        r = Rectangle(5, 2)
        d = r.__dict__.copy()

        r.update(id=10)
        d["id"] = 10
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(r.__dict__, d)

        r.update(id=10, width=5, height=17, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(r.__dict__, d)

        r.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(r.__dict__, d)

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_M_to_dictionary(self):
        '''Tests to_dictionary() signature:'''
        with self.assertRaises(TypeError) as e:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        r = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(r.to_dictionary(), d)

        r.x = 10
        r.y = 20
        r.width = 30
        r.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(r.to_dictionary(), d)

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

if __name__ == '__main__':
    unittest.main()

