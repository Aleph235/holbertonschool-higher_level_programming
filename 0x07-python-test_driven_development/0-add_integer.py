#!/usr/bin/python3
def add_integer(a, b=98):
    """add integers a and b with default value for b as 98
    a and be must be integers or floats else the function returns an 
    error message"""
    if type(a) == float:
            a = int(a)
    if type(b) == float:
            b = int(b)
    elif type(a) != int:
        raise TypeError("a must be an interger")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
