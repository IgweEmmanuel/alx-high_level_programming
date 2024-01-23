#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """
    Print x elements of list.

    Args:
        my_list (list): This is the list to print.
        x (int): This is the number of element to be printed.

    Return:
        The number of elements.
    """

    b = 0
    i = 0

    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            b += 1
        except:
            continue
    print()
    return b
