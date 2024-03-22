#!/usr/bin/python3
"""attempts to provide a N(log(N)) solution to find minimum number of
    'copy-and-paste' to get from 1 to a number"""


def minOperations(n):
    """the n(log(n)) solution"""
    number = n
    res = 0
    i = 2
    while i <= number:
        while number % i == 0:
            res += i
            number = number // i
        i += 1
    return res
