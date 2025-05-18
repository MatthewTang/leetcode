import unittest
from typing import List, Optional


class Solution:
    # # O(n), n no. of intervals
    # def insert(
    #     self, intervals: List[List[int]], newInterval: List[int]
    # ) -> List[List[int]]:
    #     res = []
    #     ns, ne = newInterval
    #     inserted = 0
    #     for s, e in intervals:
    #         if inserted:
    #             _, _e = res[-1]
    #             if s <= _e:
    #                 res[-1][1] = max(_e, e)
    #                 continue
    #             res.append([s, e])
    #             continue
    #         else:
    #             if ne < s:
    #                 res.append([ns, ne])
    #                 res.append([s, e])
    #                 inserted = 1
    #                 continue
    #             if ns > e:
    #                 res.append([s, e])
    #                 continue
    #             res.append([min(s, ns), max(e, ne)])
    #             inserted = 1
    #
    #     if not inserted:
    #         res.append(newInterval)
    #
    #     return res

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        ns, ne = newInterval
        for i, (s, e) in enumerate(intervals):
            if ne < s:
                res.append([ns, ne])
                res += intervals[i:]
                return res
            elif ns > e:
                res.append([s, e])
            else:
                ns, ne = min(s, ns), max(e, ne)

        res.append(newInterval)
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expected = [[1, 5], [6, 9]]
        result = s.insert(intervals, newInterval)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        result = s.insert(intervals, newInterval)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        intervals = []
        newInterval = [5, 7]
        expected = [[5, 7]]
        result = s.insert(intervals, newInterval)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        intervals = [[1, 5]]
        newInterval = [6, 8]
        expected = [[1, 5], [6, 8]]
        result = s.insert(intervals, newInterval)
        self.assertListEqual(result, expected)

    def test5(self):
        s = Solution()
        intervals = [[1, 5]]
        newInterval = [0, 0]
        expected = [[0, 0], [1, 5]]
        result = s.insert(intervals, newInterval)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
