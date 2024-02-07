#!/usr/bin/python3
"""Python write into file"""
import json


def save_to_json_file(my_obj, filename):
    """json representation of a file
    Args:
        my_obj: the text object (string)
    Return: the serialized file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return json.dump(my_obj, myFile)
