#!/usr/bin/python3
"""The BaseGeometry class"""


class BaseGeometry:
    """
    Class geometry
    """

    def area(self):
        """area
        Args:
            self: the object method
        Return: exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator
        Args:
            self: instance referer
            name: name
            value: integer value
        Return: value
        """
        self.name = str(name)
        if not type(value) is int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
