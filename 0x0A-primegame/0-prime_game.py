#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner of a set of prime number removal games.
    """
    if x < 1 or nums is None or x != len(nums):
        return None
    player1 = 0
    player2 = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        unset_prime_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            player1 += 1
        else:
            player2 += 1
    if player1 > player2:
        return "Ben"
    if player2 > player1:
        return "Maria"
    return None


def unset_prime_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.
       None.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
