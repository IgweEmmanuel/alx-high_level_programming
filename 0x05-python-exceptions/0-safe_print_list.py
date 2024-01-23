#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of list.
    
    Args:
        my_list (list): This is the list to print.
        x (int): This is the number of element to be printed.
    
    Return:
        The number of elements.
    """
    ans = 0
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
            ans += 1
        except IndexError:
            break
    print("")
    return (ans)
