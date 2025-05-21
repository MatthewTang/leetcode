import unittest
from typing import List, Optional
import heapq


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


# Meeting Rooms II
class Solution:
    # time: O(n^2)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 1:
            return 0
        intervals.sort(key=lambda i: i.start)
        prev_ends = [intervals[0].end]
        for i in intervals[1:]:
            s, e = i.start, i.end
            for j in range(len(prev_ends)):
                if s >= prev_ends[j]:
                    prev_ends[j] = e
                    break
            else:
                prev_ends.append(e)
        return len(prev_ends)

    # time: O(nlogn)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 1:
            return 0
        intervals.sort(key=lambda i: i.start)
        prev_ends = []
        heapq.heappush(prev_ends, intervals[0].end)
        for i in intervals[1:]:
            if prev_ends[0] <= i.start:
                heapq.heappop(prev_ends)
            heapq.heappush(prev_ends, i.end)

        return len(prev_ends)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
        expected = 2
        result = s.minMeetingRooms(intervals)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        intervals = [Interval(15, 20), Interval(5, 10), Interval(0, 40)]
        expected = 2
        result = s.minMeetingRooms(intervals)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        intervals = [Interval(4, 9)]
        expected = 1
        result = s.minMeetingRooms(intervals)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        intervals = []
        expected = 0
        result = s.minMeetingRooms(intervals)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
