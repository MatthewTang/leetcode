import unittest
from typing import List, Optional


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p: (p[1], -p[0]))
        res = 0
        ps, pe = intervals[0]

        for s, e in intervals[1:]:
            if pe <= s:
                ps, pe = s, e
            else:
                pe = min(pe, e)
                res += 1

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        expected = 1
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        intervals = [[1, 2], [1, 2], [1, 2]]
        expected = 2
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        intervals = [[1, 2], [2, 3]]
        expected = 0
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        intervals = [[1, 2], [1, 3], [3, 4], [2, 3]]
        expected = 1
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        intervals = [[1, 2], [1, 4], [3, 4], [2, 3]]
        expected = 1
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test6(self):
        s = Solution()
        intervals = [[11, 22], [1, 11], [2, 12]]
        expected = 1
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)

    def test7(self):
        s = Solution()
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        expected = 2
        result = s.eraseOverlapIntervals(intervals)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
