#!/usr/bin/python3
def print_square(size):
    """This function prints a square with #
    Args:
        size: this is the length of the square
    Return: This returns the square in # symbol
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    print('\n'.join(['#' * int(size) for _ in range(int(size))]))
