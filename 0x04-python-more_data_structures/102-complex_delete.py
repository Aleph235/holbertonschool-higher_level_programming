#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        if new_dict[key] == value:
            del new_dict[key]
        else:
            return new_dict
    return new_dict
