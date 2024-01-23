#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer.
    Args:
        value (int): The integer to print
    Return:
        TypeError or ValueError occurs is - False.
        Else it is - True
    """

    try:
        print("{:d}".format(value))
        return True
    except:
        return False
