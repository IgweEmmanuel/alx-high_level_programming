#!/usr/bin/python3
"""Python write into file"""
import json


def load_from_json_file(filename):
    """json representation of a file
    Args:
        my_obj: the text object (string)
    Return: the serialized file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return json.loads(myFile)
