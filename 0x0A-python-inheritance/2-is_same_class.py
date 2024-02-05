#!/usr/bin/python3
"""Is same class checker"""


def is_same_class(obj, a_class):
    """The function that checks for types
    Args:
        obj: this is the object
        a_class: this is the class
    Return: this returns type match
    """
    return type(obj) is a_class
