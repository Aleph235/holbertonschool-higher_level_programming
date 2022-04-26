#!/usr/bin/python3
for item in range(100):
    if item == 89:
        print(item)
    elif item % 10 > item // 10:
        print("{:02}".format(item), end=", ")
