#!/usr/bin/python3
"""Python read file"""


def read_file(filename=""):
    """This reads file
    Args:
        filename: the name of the file
    Return: the content of the file
    """
    with open(filename, 'r', encoding="utf-8") as myFile:
        print(myFile.read(), end='')
