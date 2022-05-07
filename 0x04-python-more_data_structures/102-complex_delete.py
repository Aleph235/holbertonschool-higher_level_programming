#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        if new_dict[key] == value:
            del new_dict[key]
        else:
            break
    return new_dict
