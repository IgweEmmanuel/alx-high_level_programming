#!/usr/bin/python3
"""Real definition of a rectangle"""
class Rectangle:
    """
        The code defines a rectangle
        Attributes:
            width: this is the width of the rectangle
            height: this is the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """This initializes the instance and assigns attributes
            Args:
                width: this is the width of the rectangle
                height: this is the height of the rectangle
        """
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if vlaue < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
