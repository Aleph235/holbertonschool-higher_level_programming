#!/usr/bin/python3
"""class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """instantiate the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict repr of student instance"""
        json_attr = {}
        if type(attrs) == list and all(type(attr) == str for attr in attrs):
            for attr in attrs:
                if attr in self.__dict__:
                    json_attr.update({attr: self.__dict__[attr]})
            return json_attr
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes to student with json file"""
        for key in json:
            self.__dict__.update({key: json[key]})
