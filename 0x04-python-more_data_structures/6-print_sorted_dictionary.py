#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dico = sorted(a_dictionary.items())
    for key, val in sorted_dico:
        print(f'{key}: {val}')
