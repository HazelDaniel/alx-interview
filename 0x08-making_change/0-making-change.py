#!/usr/bin/python3
"""this module attempts to provide a solution to the problem:
    determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """ Generates changes needed to reach total amount """
    if total <= 0:
        return 0
    curr = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while curr < total:
            curr += i
            temp += 1
        if curr == total:
            return temp
        curr -= i
        temp -= 1
    return -1
