#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        stringcopy = str[:n] + str[n+1:]
        return stringcopy
    else:
        return str
