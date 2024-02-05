#!/usr/bin/python3
"""This is a subclass of list that prints list super class"""


class MyList(list):
    """
    This subclass prints the list
    """


    def print_sorted(self):
        """This public instance prints the list
        """
        print(sorted(self))

