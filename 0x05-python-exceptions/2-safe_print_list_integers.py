#!/usr/bin/python3

def safe_print_list_integers (my_list=[], x=0):
    """Print the first integer x elements of a list

    Args:
        my_list (list): The list that elements will be printed from
        x (int): this is the number of elements of my_list

    Return:
        The number of elements are printed
    """
    ans = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ans += 1
        except (valueError, TypeError):
            continue
    print("")
    return (ans)
