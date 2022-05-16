#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    message_1 = "Exception: Unknown format code 'd' for object of type 'str'"
    message_2 = "Exception: unsupported format string passed to tuple.__format__"
    try:
        print("{:d}".format(value))
        return True
    except (ValueError):
        print(message_1, file=sys.stderr)
        return False
    except (TypeError):
        print(message_2, file=sys.stderr)
        return False

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = 1,4 
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))
