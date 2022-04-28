#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n < 2:
        print("0 arguments.")
    elif n > 2:
        print(f"{n - 1} arguments:")
    else:
        print("1 argument:")
    for i in range(1, n):
        if n == 2:
            print(f"{i}: {sys.argv[i]}")
        else:
            print(f"{i}: {sys.argv[i]}")
