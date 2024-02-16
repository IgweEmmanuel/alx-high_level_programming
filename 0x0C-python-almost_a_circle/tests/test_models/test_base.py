#!/usr/bin/python3
"""MOdule for Square unit tests."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests teh Base class."""

    def setUp(self):
        """imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Clean up after each test_method"""
        pass

    def test_1_nb_objectcs_private(self):
        """Check if it has a private attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_2_initialized(self):
        """Check if attribute is initialized"""
        self.assertEqual(getattr(Base, "_Base__nb_objects"),0)

    def test_3_instantiation(self):
        """Test for class object instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_4_constructor(self):
        """Test constructor signature"""
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_constructor_args(self):
        """Test for more than 2 constructor args"""
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_consecutive_instantiation(self):
        """Check for consecutive instantiation"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_sync_btw_class_and_instance_id(self):
        """Test synchronization between class and instance id"""
        b = Base()
        b = Base("foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_id(self):
        """Test for custom id"""
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_keyword(self):
        """Tests id passed as keyword arg"""
        b = Base(id=1)
        self.assertEqual(b.id, 1)

    def test_to_json_string(self):
        """Tests to_json_string() signature"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        msg = "to_json_string() missing 1 required positional argument: 'list_dictionaries'"
        self.assertEqual(str(e.exception), msg)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        list_dicts = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}, {'x':5, 'y':7, 'width':8, 'id':10}]
        expected_json_string = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, {"x": 5, "y": 7, "width": 8, "id": 10}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json_string)

    def test_from_json_string(self):
        """Test from_json_string() signature"""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        s = "from_json_string() missing 1 required positional argument: 'json_string'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        json_string = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5},{"x": 5, "y": 7, "width": 8, "id": 10}]'
        expected_list_dicts = [{'x': 1, 'y': 2, 'width': 3, 'id': 4,'height': 5},{'x': 5, 'y': 7, 'width': 8, 'id': 10}]
        self.assertEqual(Base.from_json_string(json_string), expected_list_dicts)
if __name__ == '__main__':
    unittest.main()

