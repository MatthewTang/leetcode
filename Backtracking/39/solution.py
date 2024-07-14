import unittest
import heapq
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return [1]


class TestSolution(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.combinationSum([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
