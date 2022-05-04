#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        value_sorted_list = sorted(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value_sorted_list[-1] == value:
                return key
