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
