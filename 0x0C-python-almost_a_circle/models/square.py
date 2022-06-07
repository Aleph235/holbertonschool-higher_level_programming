#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise square attributes"""
        super().__init__(width, height, x, y, id)
        size = width, height

    def __str__(self):
        """display the class"""
        return f"[Square] ({id}) {x}/{y} - {size}"
