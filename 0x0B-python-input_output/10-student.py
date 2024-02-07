#!/usr/bin/python3
"""returns dictionary description"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Initialize an empty dictionary to store the JSON representation"""
        if not attr or not isinstance(attr, list):
            return self.__dict__

        json_dict = {}

        for attr_name in attr:
            if hasattr(self, attr_name) and isinstance(attr_name, str):
                json_dict[attr_name] = getattr(self, attr_name)

        return json_dict
