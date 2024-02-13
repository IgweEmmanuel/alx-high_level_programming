#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        list_dicts = [{"id": 1, "name": "foo"}, {"id": 2, "name": "bar"}]
        expected_json_string = '[{"id": 1, "name": "foo"}, {"id": 2, "name": "bar"}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json_string)

    # Add more test cases for other methods...

if __name__ == '__main__':
    unittest.main()

