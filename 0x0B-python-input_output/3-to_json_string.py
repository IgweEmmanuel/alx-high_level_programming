#!/usr/bin/python3
"""Python write into file"""
import json


def to_json_string(my_obj):
    """json representation of a file
    Args:
        my_obj: the text object (string)
    Return: the serialized file
    """
    return json.dumps(my_obj)
