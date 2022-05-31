#!/usr/bin/python3
import json
"""returns json serialization of an object"""


def class_to_json(obj):
    """returns json serialization of an object"""
    return json.dumps(obj.__dict__)
