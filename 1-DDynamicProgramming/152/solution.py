import unittest
from typing import List, Optional


class Solution:
    # bf, time: O(n^2), space: O(1), tle
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            prod = nums[i]
            res = max(res, prod)

            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                res = max(res, prod)

        return res

    # # kadane, time: O(n), space: O(1)
    # def maxProduct(self, nums: List[int]) -> int:
    #     res = nums[0]
    #     a, b = 1, 1
    #
    #     for num in nums:
    #         a, b = max(a * num, b * num, num), min(a * num, b * num, num)
    #         res = max(res, a)
    #
    #     return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 3, -2, 4]
        expected = 6
        result = s.maxProduct(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [-2, 0, -1]
        expected = 0
        result = s.maxProduct(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [-2, -1]
        expected = 2
        result = s.maxProduct(nums)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [1, 2, -3, 4]
        expected = 4
        result = s.maxProduct(nums)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        nums = [-2, 0, 2, 5]
        expected = 10
        result = s.maxProduct(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
