#!/usr/bin/python3
"""returns json serialization of an object"""
import json


def class_to_json(obj):
    """returns json serialization of an object"""
    return json.dumps(obj.__dict__)
