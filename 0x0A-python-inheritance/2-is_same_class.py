#!/usr/bin/python3
"""returns True if the object instance of a_class ; otherwise False"""


def is_same_class(obj, a_class):
    """returns True if the object instance of a_class ; otherwise False"""
    return isinstance(type(obj), a_class)
