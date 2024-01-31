#!/usr/bin/python3
"""String representation"""


class Rectangle:
    """"
    This prints # as string representation
    """
    number_of_instances = 0
    print_symbol = '#'


    def __init__(self, width=0, height=0):
        """This returns the various functions in the class
        Args:
            width: this returns the width of the rectangle
            height: this returns the height of the rectangle
        Returns: this returns the area, perimeter and string representtion
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @width.setter
    def widthi(self, value):
        """width setter function"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter function"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return(self.__height * self.__width)

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """string representation of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return '\n'.join([str(Rectangle.print_symbol) * self.__width
                             for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
