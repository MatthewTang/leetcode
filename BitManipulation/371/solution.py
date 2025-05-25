import unittest
from typing import List, Optional


class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0
        for i in range(31):
            _a = (a >> i) & 1
            _b = (b >> i) & 1
            res |= (_a ^ _b ^ carry) << i
            carry = _a & _b

        return res

    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        a = 1
        b = 2
        expected = 3
        result = s.getSum(a, b)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        a = 2
        b = 3
        expected = 5
        result = s.getSum(a, b)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        a = 999
        b = 999
        expected = 1998
        result = s.getSum(a, b)
        self.assertEqual(result, expected)

    def test4(self):
        s = Solution()
        a = 3
        b = -2
        expected = 1
        result = s.getSum(a, b)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
