#!/bin/python3
"""Creates a list of lists for pascal_triangle"""


def binomialCoeff(n, k):
    """calculate the binomialCoeff for n and k"""
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def pascal_triangle(n):
    """Creates a list of lists for pascal_triangle"""
    l1 = []
    if n <= 0:
        return l1
    else:
        for line in range(0, n):
            l1.append([])
            for i in range(0, line + 1):
                l1[line].append(binomialCoeff(line, i))
        return l1
