import unittest
from typing import List, Optional


class Solution:
    # # bf, O(2^n)
    # def numDecodings(self, s):
    #     def dfs(i: int, j: int) -> int:
    #         _s: str = s[i:j]
    #         if _s.startswith("0"):
    #             return 0
    #         if int(_s) > 26:
    #             return 0
    #
    #         if len(s) == j:
    #             return 1
    #         if len(s) - 1 == j:
    #             r = s[j:]
    #             return 1 if int(r) > 0 else 0
    #
    #         return dfs(j, j + 1) + dfs(j, j + 2)
    #
    #     if len(s) == 1:
    #         return 1 if int(s) > 0 else 0
    #
    #     return dfs(0, 1) + dfs(0, 2)

    # # dp(td), time/space: O(n)
    # def numDecodings(self, s):
    #     cache = {}
    #
    #     def dfs(i: int, j: int) -> int:
    #         if (i, j) in cache:
    #             return cache[i, j]
    #
    #         _s: str = s[i:j]
    #         if _s.startswith("0"):
    #             cache[i, j] = 0
    #             return cache[i, j]
    #         if int(_s) > 26:
    #             cache[i, j] = 0
    #             return cache[i, j]
    #
    #         if len(s) == j:
    #             cache[i, j] = 1
    #             return cache[i, j]
    #         if len(s) - 1 == j:
    #             r = s[j:]
    #             cache[i, j] = 1 if int(r) > 0 else 0
    #             return cache[i, j]
    #
    #         cache[i, j] = dfs(j, j + 1) + dfs(j, j + 2)
    #         return cache[i, j]
    #
    #     if len(s) == 1:
    #         return 1 if int(s) > 0 else 0
    #
    #     return dfs(0, 1) + dfs(0, 2)

    # # # dp(bu), time/space: O(n)
    # def numDecodings(self, s):
    #     if len(s) == 1:
    #         return 1 if int(s) > 0 else 0
    #
    #     l = len(s)
    #     dp = [0] * l
    #     dp[-1] = 1 if int(s[-1]) > 0 else 0
    #     dp[-2] = 0 if int(s[-2]) == 0 else (dp[-1] + 1 if int(s[-2:]) < 27 else dp[-1])
    #
    #     for i in range(l - 3, -1, -1):
    #         v1 = int(s[i]) > 0
    #         v2 = v1 and int(s[i : i + 2]) < 27
    #         if v1:
    #             dp[i] += dp[i + 1]
    #         if v2:
    #             dp[i] += dp[i + 2]
    #
    #     return dp[0]

    # # dp(bu), time: O(n), space: O(1)
    def numDecodings(self, s):
        if len(s) == 1:
            return 1 if int(s) > 0 else 0

        l = len(s)
        prev2 = 1 if int(s[-1]) > 0 else 0
        prev1 = 0 if int(s[-2]) == 0 else (prev2 + 1 if int(s[-2:]) < 27 else prev2)

        for i in range(l - 3, -1, -1):
            prev = 0
            v1 = int(s[i]) > 0
            v2 = v1 and int(s[i : i + 2]) < 27
            if v1:
                prev += prev1
            if v2:
                prev += prev2
            prev1, prev2 = prev, prev1

        return prev1


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "12"
        expected = 2
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "226"
        expected = 3
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "06"
        expected = 0
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test4(self):
        sol = Solution()
        s = "1"
        expected = 1
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "0"
        expected = 0
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "2"
        expected = 1
        result = sol.numDecodings(s)
        self.assertIs(result, expected)

    def test6(self):
        sol = Solution()
        s = "111111111111111111111111111111111111111111111"
        expected = 1836311903
        result = sol.numDecodings(s)
        self.assertEqual(result, expected)

    def test7(self):
        sol = Solution()
        s = "1234"
        expected = 3
        result = sol.numDecodings(s)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
