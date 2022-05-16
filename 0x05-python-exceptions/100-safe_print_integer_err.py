#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ver:
        print('Exeption: {}'.format(ver), file=sys.stderr)
        return False
    except TypeError as ter:
        print(f'Exeption: {}'.format(ter), file=sys.stderr)
        return False
