#!/usr/bin/python3
result = ''
for i in reversed(range(97, 123)):
    if i % 2 != 0:
        result += str.upper(chr(i))
    else:
        result += chr(i)
print(result, end='')
