#!/usr/bin/python3
"""this module attempts to solve the nqueens problem"""

import sys


class Nqueens:
    """a class that has the method and util
        functions to solve the nqueens problem"""

    def __init__(self, nums):
        """the entry point into the class instance"""
        self.nums = nums
        self.board = []

    def solve(self):
        """this utility performs validation on the command line argument N
            before attempting to solve the N-queens problem"""
        self.cols = set()
        self.rows = set()
        self.pos_diag = set()
        self.neg_diag = set()
        self.res = []
        self.hash = dict()

        if (type(self.nums) is not int):
            try:
                self.nums = int(self.nums)
            except Exception:
                print("N must be a number")
                return
        if (self.nums < 4):
            print("N must be at least 4")
            return
        self.backtrack(0)
        return self.res

    def backtrack(self, r):
        """the main backtracking algorithm used in the n-queens solution"""
        if (r == self.nums):
            self.res.append(list(self.hash.values()))
            self.hash = dict()
            return

        for c in range(self.nums):
            if (c in self.cols or (r - c) in self.neg_diag or
                    (r + c) in self.pos_diag):
                continue
            self.cols.add(c)
            self.neg_diag.add(r - c)
            self.pos_diag.add(r + c)
            self.hash[f"{r}{c}"] = [r, c]
            self.board.append(self.hash[f"{r}{c}"])

            self.backtrack(r + 1)

            self.cols.remove(c)
            self.neg_diag.remove(r - c)
            self.pos_diag.remove(r + c)
            if (f"{r}{c}" in self.hash):
                self.hash.pop(f"{r}{c}")


def main():
    """the entry point into the program"""
    if __name__ != "__main__":
        return
    if (len(sys.argv) < 2):
        print("no arguments provided!")
        return
    input = sys.argv[1]
    queens = Nqueens(input)
    solution = queens.solve()
    if (not solution):
        return
    for i in solution:
        print(i)


main()
