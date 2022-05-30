#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        """raise exception for non implemeted method"""
        raise Exception("area() is not implemented")
