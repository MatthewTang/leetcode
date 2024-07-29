import unittest
import heapq
from typing import List
from functools import reduce
from collections import deque


class Grid:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __repr__(self):
        return f"{str(self.i)}, {str(self.j)}"

    def up(self):
        self.i = self.i - 1

    def down(self):
        self.i = self.i + 1

    def left(self):
        self.j = self.j - 1

    def right(self):
        self.j = self.j + 1


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return

class TestSolution(unittest.TestCase):
    def test1(self):
        s = Solution()

        g = Grid(0, 0)
        print(g)
        g.right()
        print(g)

        # print([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]][0][1])

        # self.assertTrue(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))


if __name__ == "__main__":
    unittest.main()
