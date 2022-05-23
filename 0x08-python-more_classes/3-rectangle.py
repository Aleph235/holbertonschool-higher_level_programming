#!/usr/bin/python3
"""Rectangle class with private attributes width and height"""


class Rectangle:
    """Rectangle class with private attributes width and height"""
    def __init__(self, width=0, height=0):
        """Class method to intialize the rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get class property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width property with errror checks"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get class property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height property with errror checks"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return str(self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """print the rectangle with the character #"""
        shape = ''
        if self.__width == 0 or self.__height == 0:
            shape = "\n"
        else:
            for i in range(self.__height):
                shape += ("#" * self.__width + "\n")
        return shape
