#!/usr/bin/python3
for item in range(100):
    if item == 99:
        print(item)
    else:
        print("{:02}".format(item), end=", ")
