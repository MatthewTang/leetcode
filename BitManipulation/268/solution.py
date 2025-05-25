import unittest
from typing import List, Optional


class Solution:
    # # sum, time: O(n), space: O(1)
    # def missingNumber(self, nums: List[int]) -> int:
    #     s = 0
    #     for i in range(len(nums) + 1):
    #         s += i
    #     for n in nums:
    #         s -= n
    #     return s

    # # sum(optimised), time: O(n), space: O(1)
    # def missingNumber(self, nums: List[int]) -> int:
    #     s = len(nums)
    #
    #     for i in range(len(nums)):
    #         s += i - nums[i]
    #
    #     return s

    # # xor
    # def missingNumber(self, nums: List[int]) -> int:
    #     xor = 0
    #     for i in range(len(nums) + 1):
    #         xor ^= i
    #     for num in nums:
    #         xor ^= num
    #     return xor

    # xor(optimised)
    def missingNumber(self, nums: List[int]) -> int:
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        return xor


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [3, 0, 1]
        expected = 2
        result = s.missingNumber(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [0, 1]
        expected = 2
        result = s.missingNumber(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [9,6,4,2,3,5,7,0,1]
        expected = 8
        result = s.missingNumber(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
