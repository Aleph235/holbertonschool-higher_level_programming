#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if my_list == []:
        return None
    elif n == 1:
        return my_list[0]
    my_list.sort()
    return my_list[n-1]
