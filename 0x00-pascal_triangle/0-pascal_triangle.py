#!/usr/bin/python3
"""this module attempts to solve the pascal's triangle problem"""


def pascal_triangle(n):
    """this function prints out the sequence of pascal's triangle
        given a sequence count n"""
    if (n <= 0):
        return []
    start_matrix = [[0 for _ in range(n)] for _ in range(n)]
    end_matrix = [[] for _ in range(n)]
    start_matrix[0][0] = 1
    end_matrix[0].append(1)

    for i in range(n):
        for j in range(i + 1):
            up = start_matrix[i - 1][j] if i - 1 > - 1 else 0
            up_left = start_matrix[i - 1][j - 1]\
                if j - 1 > - 1 and i - 1 > - 1 else 0
            if (i or j):
                start_matrix[i][j] = up + up_left
                end_matrix[i].append(up + up_left)

    return end_matrix
