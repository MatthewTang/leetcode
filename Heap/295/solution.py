import unittest
import heapq


# two heap
class MedianFinder:
    # two heaps, large (min-heap) and small (max-heap)
    # heaps shd be eq size
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.small) > len(self.large) + 1:
            v = -heapq.heappop(self.small)
            heapq.heappush(self.large, v)
        if len(self.large) > len(self.small) + 1:
            v = heapq.heappop(self.large)
            heapq.heappush(self.small, -v)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2

    def __repr__(self) -> str:
        return f"small:{self.small},large:{self.large}"


# insert in-order
# class MedianFinder:
#     # O(1)
#     def __init__(self):
#         self.l = []
#
#     # O(nlogn)
#     def addNum(self, num: int) -> None:
#         self.l.append(num)
#         self.l.sort()
#
#     # O(1)
#     def findMedian(self) -> float:
#         n = len(self.l)
#         middle = n // 2
#         return (self.l[middle] + self.l[~middle]) / 2
#
#     def __repr__(self) -> str:
#         return f"{self.l}"


class TestSolution(unittest.TestCase):
    def test1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertAlmostEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertAlmostEqual(mf.findMedian(), 2.0)


if __name__ == "__main__":
    unittest.main()
