import unittest
import heapq
from typing import List
from functools import reduce
from collections import deque


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # def dfs(i: int, cur: List[int]) -> None:
        #     total = reduce(lambda x, y: x + y, cur, 0)

        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return

        #     cur.append(candidates[i])
        #     dfs(i, cur)
        #     cur.pop()
        #     dfs(i + 1, cur)

        # dfs(0, [])

        def dfs(i: int, cur: List[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
            return

        dfs(0, [], 0)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        s = Solution()
        print(s.combinationSum([2, 3, 6, 7], 7))
        print(s.combinationSum([1], 1))

        # self.assertEqual(s.combinationSum([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
