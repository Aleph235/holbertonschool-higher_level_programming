#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        elements_printed_count = 0
        for i in range(0, x):
            print(f'{my_list[i]}', end="")
            elements_printed_count += 1
    except IndexError:
        pass
    return elements_printed_count
