#!/usr/bin/python3
"""This wil define integer addition"""


def add_integer(a, b=98):
    """This function returns sum of a and b
    Args:
        a: the first integer
        b: the second integer
    Return: This programme returns integer
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return (a + b)
