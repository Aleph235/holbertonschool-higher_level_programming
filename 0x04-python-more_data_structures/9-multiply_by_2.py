#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_by_2 = a_dictionary.copy()
    for key, value in dic_by_2.items():
        dic_by_2.update({key: value*2})
    return dic_by_2
