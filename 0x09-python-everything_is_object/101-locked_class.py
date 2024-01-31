#!/usr/bin/python3
"""Locked class"""

class LockedClass:
    """
    This is a locked class
    """
    __slots__ = ('first_name',)

    def __init__(self, first_name):
        self.first_name = first_name

# Example usage:
obj = LockedClass("John")
print(obj.first_name)  # Accessing allowed attribute

# Attempting to create a new attribute dynamically
try:
    obj.last_name = "Doe"  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

