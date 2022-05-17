#!/usr/bin/python3
"""square class with private attribute size"""


class Square:
    """square class with private attribute size"""
    def __init__(self, size=0):
        """Class method to initialize the square object"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
