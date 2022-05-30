#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """raise exception for non implemeted method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """validate value if it is an int and strictly positive"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
