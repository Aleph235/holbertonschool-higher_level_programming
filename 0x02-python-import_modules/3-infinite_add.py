#!/usr/bin/python3
import sys
n = len(sys.argv)
result = 0
for i in range(1, n):
    result += int(sys.argv[i])
print(f'{result}')
