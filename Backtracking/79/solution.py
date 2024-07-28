import unittest
import heapq
from typing import List
from functools import reduce
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertTrue(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))


if __name__ == "__main__":
    unittest.main()
