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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))
