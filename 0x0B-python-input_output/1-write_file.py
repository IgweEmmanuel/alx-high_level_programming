#!/usr/bin/python3
"""Python write into file"""


def write_file(filename="", text=""):
    """write file
    Args:
        filename: name of file
        text: text to fill file with
    Return: the writen file
    """
    count = 0
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(text)
        return len(text)
