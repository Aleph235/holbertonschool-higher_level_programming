#!/usr/bin/python3
"""returns True if the object is instance amd subclass of a class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is instance amd subclass of a class"""
    return isinstance(obj, a_class) and issubclass(a_class, a_class)
