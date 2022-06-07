#!/usr/bin/python3
"""Define Base class"""
import json


class Base:
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise base attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
