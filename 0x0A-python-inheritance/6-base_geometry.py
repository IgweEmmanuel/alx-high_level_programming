#!/usr/bin/python3
"""This is geometry class with public instance"""


class BaseGeometry:
    """
    BaseGeometry
    """

    def area(self):
        """raises exception on areas
        Args:
            self: this is instance of object
        Return: exception
        """
        raise Exception("area() is not implemented")
