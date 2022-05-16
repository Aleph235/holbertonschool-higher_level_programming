#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    err_message = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print(err_message, file=sys.stderr)
        return False
