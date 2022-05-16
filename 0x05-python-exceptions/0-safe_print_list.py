#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed_count = 0

    for i in range(0, x):
        try:
            print(f'{my_list[i]}', end="")
            elements_printed_count += 1
        except IndexError:
            break
    return elements_printed_count
