#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """
    This returns area and perimeter of a rectangle
    Attribute:
        area: the area of rectangle
        perimeter: the perimeter of a rectangle
    """
    def __init__(self, width=0, height=0):
        """This outputs area and perimeter
        Args:
            width: this is the width of the rectangle
            height: this is the height of the rectangle
        """
        self.width = width
        self.height = height
        self.area
        self.perimeter

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """value: this sets teh width value
        """
        if not isinstance(value, int):
            raise TypeEror("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height: this is the height of the rectangle
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
