#!/usr/bin/python3
"""this module attempts to solve a problem
    related to the rotation of a 2-dimensional matrix"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees in a clockwise manner
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """the call to the procedure"""
    rotate_2d_matrix(matrix)
    print(matrix)
