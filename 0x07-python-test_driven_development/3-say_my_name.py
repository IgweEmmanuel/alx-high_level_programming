#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """This function prints first and last name
    Args:
        first_name: this is the first name parameter
        last_name: this is the last name parameter
    Return: it returns a string
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is " + first_name + " " + last_name)
