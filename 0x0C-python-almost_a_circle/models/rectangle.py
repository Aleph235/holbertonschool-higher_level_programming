#!/usr/bin/python3
"""class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get class property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width property with error checks"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get class property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height property with error checks"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get class property x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x property with error checks"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get class property y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y property with error checks"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def area(self):
        """calculates the area of the triangle"""
        return self.width * self.height

    def display(self):
        """displays the rectangle with character #"""
        if self.area == 0:
            print()
        for j in range(self.y):
            if self.area > 0:
                print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print class rectangle"""
        return f"[Rectangle] ({self.id})"/
        " {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update rectangle instance"""
        list = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, list[i], args[i])
        for key, value in kwargs.items():
            if key in list:
                setattr(self, key, value)
