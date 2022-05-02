#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[0] == "C":
            new_str = my_string[1:]
        if my_string[i] == "c" and i > 0:
            new_str = my_string[:i] + my_string[i+1:]
            if my_string[i] == "C" and i > 0:
                new_str = new_str[:i] + new_str[i+1:]
    return new_str

print(no_c("Chicago"))
print(no_c("Best School"))
