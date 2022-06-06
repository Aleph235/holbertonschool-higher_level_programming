#!/bin/python3
"""base class"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialiase base class"""
        if id is None:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1
        else:
            self.id = id
