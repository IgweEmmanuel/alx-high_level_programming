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
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter 
    def width(self, value):
        try:
            if not type(value) is int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if not type(value) is int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
        
        self.__height = value
