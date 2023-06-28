#!/usr/bin/python3
"""defines a class with name square"""


class Square:
    """This class defines a squre with no publis classes"""
    def __init__(self, size=0):
        """intiaize a square.
        Args:
            size (int): This defines the size of the square.
        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """int: Return the area."""
        return self.__size * self.__size
