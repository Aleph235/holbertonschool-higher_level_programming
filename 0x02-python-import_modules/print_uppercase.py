#!/usr/bin/python3
def print_upper():
    for i in range(65, 91):
        if i == 90:
            print(chr(i))
        else:
            print(chr(i), end='')
