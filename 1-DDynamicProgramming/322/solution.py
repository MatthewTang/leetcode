import unittest
from typing import List, Optional


class Solution:
    # bf, O(c^a), given c no. of coins, a amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(c, remaining):
            if remaining == 0:
                return 0

            if c > remaining:
                return float("infinity")

            if c == remaining:
                return 1

            _count = float("infinity")
            for coin in coins:
                _count = min(dfs(coin, remaining - c), _count)

            return _count + 1

        res = float("infinity")
        for coin in coins:
            count = dfs(coin, amount)
            res = min(res, count)
        return -1 if res == float("infinity") else res

    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(c, remaining):
            if remaining == 0:
                return 0

            if c > remaining:
                return float("infinity")

            if c == remaining:
                return 1

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

    # # incorrect: not necessary max out larger coins first
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     coins.sort()
    #     count = 0
    #     i = len(coins) - 1
    #     while amount > 0 and i >= 0:
    #         coin = coins[i]
    #         remaining = amount - coin
    #         if remaining == 0:
    #             count += 1
    #             break
    #         if remaining > 0:
    #             count += 1
    #             amount = remaining
    #             continue
    #         if remaining < 0:
    #             if i == 0:
    #                 count = -1
    #                 break
    #             i -= 1
    #     return count


class Test(unittest.TestCase):
    # def test1(self):
    #     s = Solution()
    #     coins = [1, 2, 5]
    #     amount = 11
    #     expected = 3
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)
    #
    # def test2(self):
    #     s = Solution()
    #     coins = [2]
    #     amount = 3
    #     expected = -1
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)
    #
    # def test3(self):
    #     s = Solution()
    #     coins = [1]
    #     amount = 0
    #     expected = 0
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)
    #
    # def test4(self):
    #     s = Solution()
    #     coins = [1, 2, 5]
    #     amount = 100
    #     expected = 20
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)
    #
    # def test5(self):
    #     s = Solution()
    #     coins = [2, 5, 10, 1]
    #     amount = 27
    #     expected = 4
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)

    def test6(self):
        s = Solution()
        coins = [186, 419, 83, 408]
        amount = 6249
        expected = 20
        result = s.coinChange(coins, amount)
        self.assertIs(result, expected)

    # def test7(self):
    #     s = Solution()
    #     coins = [70, 177, 394, 428, 427, 437, 176, 145, 83, 370]
    #     amount = 7582
    #     expected = 18
    #     result = s.coinChange(coins, amount)
    #     self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
