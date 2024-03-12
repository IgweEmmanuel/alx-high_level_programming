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

    def to_json(self, attrs=None):
        """Initialize an empty dictionary to store the JSON representation"""
        a = all(isinstance(attr, str) for attr in attrs)
        if isinstance(attrs, list) and a:
            b = for attr in attrs if hasattr(self, attr)
            return {attr: getattr(self, attr) b}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload from json
        Args:
            self: instance of object
            json: hson file
        """
        for key, value in json.items():
            setattr(self, key, value)
