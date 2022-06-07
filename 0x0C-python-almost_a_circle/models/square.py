#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise square attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """display the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
