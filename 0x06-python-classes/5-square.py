#!/usr/bin/python3
"""square class with private attribute size"""


class Square:
    """square class with private attribute size"""
    def __init__(self, size=0):
        """Class method to initialize the square object"""
        self.size = size

    @property
    def size(self):
        """get class property size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size property with error checks"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #:
        if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
