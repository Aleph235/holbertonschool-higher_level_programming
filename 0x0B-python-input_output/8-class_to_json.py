#!/usr/bin/python3
"""returns json serialization of an object"""


def class_to_json(obj):
    """returns json serialization of an object"""
    return obj.__dict__
