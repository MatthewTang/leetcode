import unittest
from typing import List, Optional


class Solution:
    # kadane, time: O(n), space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]

        for num in nums[1:]:
            currSum = max(0, currSum) + num
            maxSum = max(maxSum, currSum)

        return maxSum


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        result = s.maxSubArray(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1]
        expected = 1
        result = s.maxSubArray(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [5, 4, -1, 7, 8]
        expected = 23
        result = s.maxSubArray(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
