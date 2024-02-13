#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instance creator
        Args:
            self: object instance
            id: input parameter
        Result: increment and store class object to id
        """

        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)     # Create a dummy Square instance
        else:
            raise ValueError("Invalid class name")

        dummy.update(**dictionary)  # Update the dummy instance with the provided dictionary
        return dummy


    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        instances = [cls.create(**dict_obj) for dict_obj in list_dicts]
        return instances
