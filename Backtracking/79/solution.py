import unittest
import heapq
from typing import List, Set, Tuple
from functools import reduce
from collections import deque


class Solution:
    # time: O(m*n*4^k), where m no. of row,, n no. of cols, k is word.length, space: O(min(k,m*n))
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(grid: Tuple[int], visited: Set[Tuple[int, int]], t: int) -> bool:
            i, j = grid
            if i < 0 or j < 0:
                return False
            if i >= ROW or j >= COL:
                return False
            if grid in visited:
                return False
            target = word[t]
            char = board[i][j]
            if char != target:
                return False
            if t == len(word) - 1:
                return True

            visited.add(grid)
            for dr, dc in directions:
                if dfs((i + dr, j + dc), visited, t + 1):
                    return True
            visited.remove(grid)

            return False

        for i in range(ROW):
            for j in range(COL):
                if dfs((i, j), set(), 0):
                    return True
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        s = Solution()
        self.assertTrue(s.exist(board, word))

    def test2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        s = Solution()
        self.assertTrue(s.exist(board, word))

    def test3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        s = Solution()
        self.assertFalse(s.exist(board, word))

    def test4(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"
        s = Solution()
        self.assertTrue(s.exist(board, word))


if __name__ == "__main__":
    unittest.main()
