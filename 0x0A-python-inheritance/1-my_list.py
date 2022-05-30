#!/usr/bin/python3
""" Class MyList that inherits list and can sort ints"""


class MyList(list):
    """ Class MyList that inherits list and can sort ints"""
    def print_sorted(self):
        """print sorted list in ascending order"""
        return print(sorted(self))
