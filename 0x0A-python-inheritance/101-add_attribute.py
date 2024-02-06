#!/usr/bin/python3
"""adds a new attriubte if possible"""


def add_attribute(obj, a, b):
    """adds new attriubte
    Args:
        obj: object
        a: attribute name
        b: attriubte value
    Return: returns new attriubte
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[a] = b
    else:
        raise TypeError("can't add new attribute")
