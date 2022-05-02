#!/usr/bin/python3
def no_c(my_string):
    global new_str
    for i in range(len(my_string)):
        if my_string[0] == "C" and my_string[i] == "c":
            new_str = my_string[1:i] + my_string[i+1:]
        elif my_string[i] in ("c", "C"):
            new_str = my_string[:i] + my_string[i+1:]
    return new_str
