#!/usr/bin/python3
"""Python write into file"""


def append_write(filename="", text=""):
    """write file
    Args:
        filename: name of file
        text: text to fill file with
    Return: the writen file
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        myFile.write(text)
        return len(text)
