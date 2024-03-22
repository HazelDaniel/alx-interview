#!/usr/bin/python3
def minOps(number):
    res = 0
    i = 2
    while i <= number:
        while number % i == 0:
            res += i
            number = number // i
        i += 1
    return res
