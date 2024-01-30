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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be an integer")
        else:
            self.__height = value
