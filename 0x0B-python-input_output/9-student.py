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

    def to_json(self):
        """Initialize an empty dictionary to store the JSON representation"""
        json_dict = {}

        for attr_name in ['first_name', 'last_name', 'age']:
            # Get the value of the attribute
            attr_value = getattr(self, attr_name)
            # Add the attribute and its value to the JSON dictionary
            json_dict[attr_name] = attr_value

        return json_dict
