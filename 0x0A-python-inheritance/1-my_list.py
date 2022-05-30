#!/usr/bin/python3
""" Class MyList that inherits list and can sort ints"""

class MyList(list):
    """ Class MyList that inherits list and can sort ints"""
    def print_sorted(self):
        """print sorted list in ascending order"""
        sorted_l = self[:]
        for i in range(1, len(sorted_l)):
            a = sorted_l[i]
            j = i - 1

            while j >= 0 and a < sorted_l[j]:
                sorted_l[j + 1] = sorted_l[j]
                j -= 1

            sorted_l[j + 1] = a
        print(sorted_l)
