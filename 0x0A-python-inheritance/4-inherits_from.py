#!/usr/bin/python3
"""Returns true if object is an instance of a class"""


def inherits_from(obj, a_class):
    """Returns true or fals
    Args:
        obj: object to check
        a_class: class to check for
    Return: true or false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
