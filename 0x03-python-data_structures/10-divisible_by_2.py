#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    truth_list = []
    for item in my_list:
        if item % 2 == 0:
            truth_list.append(True)
        else:
            truth_list.append(False)
    return truth_list
