#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """instantiator
        """
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }

    def update(self, *args, **kwargs):
        if args:
            super().update(*args)
            return
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
