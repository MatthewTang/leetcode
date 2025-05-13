import unittest
from typing import List, Optional


class Solution:
    # # bf, O(c^a), given c no. of coins, a amount
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     def dfs(coin, remaining):
    #         if remaining == 0:
    #             return 0
    #
    #         if coin > remaining:
    #             return float("infinity")
    #
    #         _count = float("infinity")
    #         for _coin in coins:
    #             _count = min(dfs(_coin, remaining - coin), _count)
    #
    #         return _count + 1
    #
    #     res = float("infinity")
    #     for coin in coins:
    #         count = dfs(coin, amount)
    #         res = min(res, count)
    #     return -1 if res == float("infinity") else res

    # O(c*a*c) = O(c*a)
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(c, remaining):
            if remaining == 0:
                return 0

            if c > remaining:
                return float("infinity")

            if (c, remaining) in cache:
                return cache[c, remaining]

            _count = float("infinity")
            for coin in coins:
                _count = min(dfs(coin, remaining - c), _count)

            cache[c, remaining] = _count + 1
            return cache[c, remaining]

        res = float("infinity")
        for coin in coins:
            count = dfs(coin, amount)
            res = min(res, count)
        return -1 if res == float("infinity") else res

    # # bf: time: O(2^a), a is amount, bc smallest c can be 1, space: O(a)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     def dfs(i, amount):
    #         if amount == 0:
    #             return 0
    #         if amount < 0:
    #             return float("infinity")
    #         if i == len(coins):
    #             return float("infinity")
    #         left = dfs(i, amount - coins[i]) + 1
    #         right = dfs(i + 1, amount)
    #         return min(left, right)
    #
    #     res = dfs(0, amount)
    #     return -1 if res == float("infinity") else res

    # # dp(td), tim: O(a*c), space: O(a*c)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     cache = {}
    #
    #     def dfs(i, amount):
    #         if amount == 0:
    #             return 0
    #         if amount < 0:
    #             return float("infinity")
    #         if i == len(coins):
    #             return float("infinity")
    #         if (i, amount) in cache:
    #             return cache[i, amount]
    #
    #         left = dfs(i, amount - coins[i]) + 1
    #         right = dfs(i + 1, amount)
    #         cache[i, amount] = min(left, right)
    #         return cache[i, amount]
    #
    #     res = dfs(0, amount)
    #     return -1 if res == float("infinity") else res

    # dp(bu), time: O(a*c), space: O(a)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        coins = [2]
        amount = 3
        expected = -1
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        coins = [1]
        amount = 0
        expected = 0
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        coins = [1, 2, 5]
        amount = 100
        expected = 20
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        coins = [2, 5, 10, 1]
        amount = 27
        expected = 4
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test6(self):
        s = Solution()
        coins = [186, 419, 83, 408]
        amount = 6249
        expected = 20
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test7(self):
        s = Solution()
        coins = [70, 177, 394, 428, 427, 437, 176, 145, 83, 370]
        amount = 7582
        expected = 18
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test8(self):
        s = Solution()
        coins = [413, 213, 453, 20, 150, 321, 254, 396, 487, 234]
        amount = 5629
        expected = 13
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    def test9(self):
        s = Solution()
        coins = [2]
        amount = 3
        expected = -1
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
