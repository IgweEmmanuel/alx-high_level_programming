#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """class that inherits int class"""

    def __eq__(self, value):
        """equal to 
        Args:
            self: instantiator
            value: the sign ==
        Return: returns !=
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """not equal to
        Args:
            self: instantiator
            value: the != sign
        Return: returns ==
        """
        return super().__eq__(value)
