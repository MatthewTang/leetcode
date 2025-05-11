import unittest
from typing import List, Optional


class Solution:
    # # bf, tim: O(2^n), where n = max(n,m), where n len(text1), m len(text2), TLE, space: O(max(m,n))
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def dfs(i, j):
    #         if i >= len(text1) or j >= len(text2):
    #             return 0
    #
    #         if text1[i] == text2[j]:
    #             return 1 + dfs(i + 1, j + 1)
    #
    #         return max(dfs(i + 1, j), dfs(i, j + 1))
    #
    #     return dfs(0, 0)

    # # dp(td), time: O(n*m), where n len(text1), m len(text2), space: O(m*n)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     cache = {}
    #
    #     def dfs(i, j):
    #         if i >= len(text1) or j >= len(text2):
    #             return 0
    #         if (i, j) in cache:
    #             return cache[i, j]
    #
    #         if text1[i] == text2[j]:
    #             cache[i, j] = 1 + dfs(i + 1, j + 1)
    #         else:
    #             cache[i, j] = max(dfs(i + 1, j), dfs(i, j + 1))
    #
    #         return cache[i, j]
    #
    #     return dfs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[j], prev = prev + 1, dp[j]
                else:
                    dp[j], prev = max(dp[j + 1], dp[j]), dp[j]

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        text1 = "cat"
        text2 = "crabt"
        expected = 3
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        text1 = "abcd"
        text2 = "abcd"
        expected = 4
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        text1 = "abc"
        text2 = "def"
        expected = 0
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
