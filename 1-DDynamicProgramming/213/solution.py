import unittest
from typing import List, Optional
from functools import lru_cache


class Solution:
    # # bf, time: O(2^(n/2)), space: O(n)
    # def rob(self, nums: List[int]) -> int:
    #     def dfs(i, first):
    #         if i >= len(nums):
    #             return 0
    #         if first and i == len(nums) - 1:
    #             return 0
    #
    #         return nums[i] + max(dfs(i + 2, first), dfs(i + 3, first))
    #
    #     if len(nums) < 3:
    #         return max(nums)
    #
    #     return max(dfs(0, True), dfs(1, False), dfs(2, False))

    # # dp-td(built-in cache), time: O(n), space: O(n)
    # def rob(self, nums: List[int]) -> int:
    #     @lru_cache
    #     def dfs(i, first):
    #         if i >= len(nums):
    #             return 0
    #         if first and i == len(nums) - 1:
    #             return 0
    #
    #         return nums[i] + max(dfs(i + 2, first), dfs(i + 3, first))
    #
    #     if len(nums) < 3:
    #         return max(nums)
    #
    #     return max(dfs(0, True), dfs(1, False), dfs(2, False))

    # # dp-td, time: O(n), space: O(n)
    # def rob(self, nums: List[int]) -> int:
    #     cache = {}
    #     l = len(nums)
    #
    #     def dfs(i, first):
    #         if i >= l:
    #             return 0
    #
    #         if i in cache:
    #             if first in cache[i]:
    #                 return cache[i][first]
    #
    #         if first and i == l - 1:
    #             return 0
    #
    #         res = nums[i] + max(dfs(i + 2, first), dfs(i + 3, first))
    #         cache[i] = {first: res}
    #         return res
    #
    #     if l <= 3:
    #         return max(nums)
    #
    #     return max(dfs(0, True), dfs(1, False), dfs(2, False))

    # # dp-bu, time: O(n), space: O(1)
    # def rob(self, nums: List[int]) -> int:
    #     l = len(nums)
    #
    #     if l <= 3:
    #         return max(nums)
    #
    #     # first
    #     a, b = nums[l - 2], nums[l - 3]
    #     i = l - 4
    #     c = a + nums[i]
    #     while i > 0:
    #         i -= 1
    #         a, b, c = b, c, nums[i] + max(a, b)
    #
    #     # second & third
    #     x, y = nums[l - 1], nums[l - 2]
    #     j = l - 3
    #     z = x + nums[j]
    #     while j > 1:
    #         j -= 1
    #         x, y, z = y, z, nums[j] + max(x, y)
    #
    #     return max(c, y, z)

    # dp-bu(optimised), time: O(n), space: O(1)
    def rob(self, nums: List[int]) -> int:
        def helper(_nums: List[int]) -> int:
            l = len(_nums)
            a, b = _nums[l - 1], _nums[l - 2]
            i = l - 3
            z = a + _nums[i]
            while i >= 0:
                i -= 1
                a, b, z = b, z, _nums[i] + max(a, b)
            return max(a, b)

        return max(helper(nums[1:]), helper(nums[:-1]))


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 3, 2]
        expected = 3
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5]
        expected = 8
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5, 6]
        expected = 12
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        nums = [
            226,
            174,
            214,
            16,
            218,
            48,
            153,
            131,
            128,
            17,
            157,
            142,
            88,
            43,
            37,
            157,
            43,
            221,
            191,
            68,
            206,
            23,
            225,
            82,
            54,
            118,
            111,
            46,
            80,
            49,
            245,
            63,
            25,
            194,
            72,
            80,
            143,
            55,
            209,
            18,
            55,
            122,
            65,
            66,
            177,
            101,
            63,
            201,
            172,
            130,
            103,
            225,
            142,
            46,
            86,
            185,
            62,
            138,
            212,
            192,
            125,
            77,
            223,
            188,
            99,
            228,
            90,
            25,
            193,
            211,
            84,
            239,
            119,
            234,
            85,
            83,
            123,
            120,
            131,
            203,
            219,
            10,
            82,
            35,
            120,
            180,
            249,
            106,
            37,
            169,
            225,
            54,
            103,
            55,
            166,
            124,
        ]
        expected = 7102
        result = s.rob(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
