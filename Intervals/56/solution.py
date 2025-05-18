import unittest
from typing import List, Optional


class Solution:
    # O(n*log(n))
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = []
        ps, pe = intervals[0]

        for s, e in intervals[1:]:
            if pe < s:
                res.append([ps, pe])
                ps, pe = s, e
            else:
                ps, pe = min(ps, s), max(e, pe)

        res.append([ps, pe])
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        result = s.merge(intervals)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        result = s.merge(intervals)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        intervals = [[1, 4]]
        expected = [[1, 4]]
        result = s.merge(intervals)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        intervals = [[1, 4], [0, 0]]
        expected = [[0, 0], [1, 4]]
        result = s.merge(intervals)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
