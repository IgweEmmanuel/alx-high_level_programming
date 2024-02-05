#!/usr/bin/python3
"""This looks up for all the attriubte and methods in a class and prints them"""


def lookup(obj):
    """This is the method that returns teh list of available attrubutes and methods"""

    return [attr for attr in dir(obj)]
