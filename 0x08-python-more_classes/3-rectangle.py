#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """"
    This prints area and perimeter of a rectangle and with # as string representation
    """
    def __init__(self, width=0, height=0):
        """This returns the various functions in the class
        Args:
            width: this returns the width of the rectangle
            height: this returns the height of the rectangle
        Returns: this returns the area, perimeter and string representtion
        """
        self.height = height
        self.width = width
        self.perimeter
        self.area

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        return 2 * (self.__height + self.__width)
    def perimeter(self, width, height):
        if width == 0 or height == 0:
            self.perimeter = 0
        self.perimeter = (2 * (width + height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value)
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        if value == 0:
            return ""
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        if value == 0:
            return ""
        self.__height = value

