#!/usr/bin/python3
"""Python write into file"""


def write_file(filename="", text=""):
    """write file
    Args:
        filename: name of file
        text: text to fill file with
    Return: the writen file
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        if not myFile:
            myFile.read()
        else:
            myFile.write(text)

