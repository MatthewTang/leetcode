class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # # sol 1 brute force
        # out = 0
        # for b in range(len(prices)):
        #     for s in range(b + 1, len(prices)):
        #         buy = prices[b]
        #         sell = prices[s]
        #         profit = sell - buy
        #         out = max(out, profit)
        #
        # return out
        #
        # # time complexity: O(n^2)
        # # space complexity: O(1)

        # # sol 2 sliding window
        # if len(prices) < 2:
        #     return 0
        #
        # b = 0
        # s = 1
        # out = max(0, prices[s] - prices[b])
        # while s < len(prices) - 1 or b < s - 1:
        #     if b == s - 1:
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     if s == len(prices) - 1:
        #         b += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     if prices[b + 1] < prices[b]:
        #         b += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     else:
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        # return out
        #
        # # # time complexity: O(1)
        # # # space complexity: O(1)
        # # wrong for [2,4,1,11,7], expects 10, output 9

        # # sol 3
        # if len(prices) < 2:
        #     return 0
        #
        # b = 0
        # s = 1
        # out = max(0, prices[s] - prices[b])
        # while s < len(prices) - 1 or b < s - 1:
        #
        #     if b == s - 1:
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     if s == len(prices) - 1:
        #         b += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     if prices[b + 1] < prices[b]:
        #         b += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     if prices[s] < prices[b]:
        #         b = s
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     else:
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        # return out

        # # sol 4
        # b = 0
        # s = 1
        # out = 0
        # while s < len(prices) - 1:
        #     if prices[s] < prices[b]:
        #         b = s
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        #     else:
        #         s += 1
        #         out = max(out, prices[s] - prices[b])
        #         continue
        #
        # return out

        # sol 5
        l, r = 0, 1
        out = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                out = max(out, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return out


if __name__ == "__main__":
    s = Solution()
    tests = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [0],
        [2, 4, 1, 11, 7],
        [4, 5, 3, 1, 6, 7],
        [5, 3, 4, 11, 7],
    ]

    for test in tests:
        print(s.maxProfit(test))
