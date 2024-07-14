import unittest


class MedianFinder:
    # O(1)
    def __init__(self):
        self.l = []

    # O(nlogn)
    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()

    # O(1)
    def findMedian(self) -> float:
        n = len(self.l)
        middle = n // 2
        return (self.l[middle] + self.l[~middle]) / 2

    def __repr__(self) -> str:
        return f"{self.l}"


class TestSolution(unittest.TestCase):
    def test1(self):
        mf = MedianFinder()
        print(mf)
        mf.addNum(1)
        print(mf)
        mf.addNum(2)
        print(mf)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)


if __name__ == "__main__":
    unittest.main()
