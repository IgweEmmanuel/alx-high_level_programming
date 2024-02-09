#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    The rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiator
        """
        super().__init__(id)
        self.width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def width(self):
        return self.__width

    def width(self, width):
        self.__width = width

    
    def height(self):
        return self.__height

    def height(self, height):
        self.__height = height


    
    def x(self):
        return self.__x

    def x(self, x):
        self.__x = x


    
    def y(self):
        return self.__y

    def y(self, y):
        self.__y = y
