#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        value_sorted_dictionary = sorted(a_dictionary.values())
        return value_sorted_dictionary[len(value_sorted_dictionary)-1]
