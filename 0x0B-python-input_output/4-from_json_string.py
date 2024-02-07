#!/usr/bin/python3
"""Python write into file"""
import json


def from_json_string(my_str):
    """json representation of a file
    Args:
        my_obj: the text object (string)
    Return: the serialized file
    """
    return json.loads(my_str)
