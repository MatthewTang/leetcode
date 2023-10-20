class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # # sol 1, only check right, failed
        # longest = 0
        #
        # for i in range(len(s)):
        #     remain = k
        #     curr = 1
        #     char = s[i]
        #     for j in range(i + 1, len(s)):
        #         _char = s[j]
        #         if _char == char:
        #             curr += 1
        #             longest = max(longest, curr)
        #             continue
        #
        #         else:
        #             if remain == 0:
        #                 break
        #             else:
        #                 curr += 1
        #                 longest = max(longest, curr)
        #                 remain -= 1
        #
        # return longest
        # # time complexity: O(n^2)

        # # sol 2, check both left and right, failed
        # out = 0
        # for i in range(len(s)):
        #     c = s[i]
        #
        #     curr = 1
        #     remain = k
        #     r = i + 1
        #     while r < len(s) and (remain > 0 or s[r] == c):
        #         if s[r] != c:
        #             remain -= 1
        #         r += 1
        #         curr += 1
        #         out = max(out, curr)
        #
        #     _remain = k
        #     _curr = 1
        #     l = i - 1
        #     while l >= 0 and (_remain > 0 or s[l] == c):
        #         if s[l] != c:
        #             _remain -= 1
        #         l -= 1
        #         _curr += 1
        #         out = max(out, _curr)
        #
        # return out
        # # time complexity: O(n^2)

        # sliding window

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
    print(s.characterReplacement("AABABBA", 1))
    print(s.characterReplacement("AAAA", 0))
    print(s.characterReplacement("ABBB", 2))
    print(s.characterReplacement("BAAAB", 2)) # expected 5
