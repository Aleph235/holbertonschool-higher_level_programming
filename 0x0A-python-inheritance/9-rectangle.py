#!/usr/bin/python3
"""class rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """initialising rectangle"""
        self.__width = width
        self.__height = height
        super().__init__()

    def area(self.width, self.height):
        """calculates the area of a Rectangle"""
        return self.width * self.height

    def __str__(self):
        """print the retangle"""
        return f"[Rectangle] {width}/{height}"
