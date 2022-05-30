#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    return issubclass(a_class, a_class)
