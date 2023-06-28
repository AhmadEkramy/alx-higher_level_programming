#!/usr/bin/python3
"""Define a class with name Square."""


class Square:
    """Represent the classs."""

    def __init__(self, size=0):
        """Initialize another Square.

        Args:
            size (int): The size of the other square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
