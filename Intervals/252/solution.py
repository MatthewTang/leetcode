import unittest
from typing import List, Optional


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


# Meeting rooms
class Solution:
    # bf, time: O(n^2)
    def canAttendMeetings(self, intervals: List[Interval]):
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)):
            e = intervals[i].end
            for j in range(i + 1, len(intervals)):
                s = intervals[j].start
                if s < e:
                    return False
        return True

    # time: O(nlogn)
    def canAttendMeetings(self, intervals: List[Interval]):
        intervals.sort(key=lambda i: i.start)
        if len(intervals) < 1:
            return True
        pe = intervals[0].end
        for i in intervals[1:]:
            if i.start < pe:
                return False
            pe = i.end

        return True


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        expected = False
        result = s.canAttendMeetings(intervals)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        intervals = [Interval(5, 8), Interval(9, 15)]
        expected = True
        result = s.canAttendMeetings(intervals)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        intervals = [Interval(0, 8), Interval(8, 10)]
        expected = True
        result = s.canAttendMeetings(intervals)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        intervals = [Interval(5, 10), Interval(0, 4)]
        expected = True
        result = s.canAttendMeetings(intervals)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        intervals = []
        expected = True
        result = s.canAttendMeetings(intervals)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
