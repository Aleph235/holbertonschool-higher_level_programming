#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    n = len(sys.argv)
    operators = ('+','-','*','/')
    def apply_operation(a, b):
        """applies the intended operation to two integers"""
        if sys.argv[2] == '+':
            return add(a, b)
        elif sys.argv[2] == '-':
            return sub(a, b)
        elif sys.argv[2] == '*':
            return mul(a, b)
        elif sys.argv[2] == '/':
            try:
                return div(a, b)
            except ZeroDivisionError as e:
                print("You can not divide by 0")
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f'{a} {sys.argv[2]} {b} = {apply_operation(a, b)}')
