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
        self.name = str
        if not type(value) is int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """sets the attributes
        Args: self: object instantiator
            width: width of the rectangle
            height: height of the rectangle
        Return: the rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__width = height
