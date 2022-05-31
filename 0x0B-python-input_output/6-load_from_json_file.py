#!/usr/bin/python3
import json
"""function that creates an
object from a JSON file"""


def load_from_json_file(filename):
    """function that creates an
    object from a JSON file"""
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)
