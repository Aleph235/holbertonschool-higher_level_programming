#!/usr/bin/python3
"""function that returns an object represented by JSON string"""
import json


def from_json_string(my_str):
    """function that returns an object represented by JSON string"""
    return json.loads(my_str)
