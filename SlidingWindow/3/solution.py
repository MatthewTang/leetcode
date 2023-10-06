class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # # try 1
        # out = 0
        # longest = set([])
        #
        # for i in range(len(s)):  # O(n)
        #     if s[i] in longest:  # O(1)
        #         if len(longest) > out:
        #             out = len(longest)
        #             outstr = longest.copy()  # O(m) m <= n
        #         longest.clear()  # O(1)
        #     longest.add(s[i])  # O(1)
        #
        # return out, outstr
        #
        # # time complexity: O(n * m) with outstr, O(n) without
        # # space complexity: longest set: O(n)
        # # doesn't work for " ", expected 1, output 0

        # # try 2
        # out = 0
        # longest = set([])
        #
        # for i in range(len(s)):  # O(n)
        #     if s[i] in longest:  # O(1)
        #         out = max(out, len(longest))
        #         longest.clear()  # O(1)
        #     longest.add(s[i])  # O(1)
        #
        # return max(out, len(longest))
        #
        # # time complexity: O(n)
        # # space complexity: longest set: O(n)
        # # doesn't work for "dvdf", expected 3, output 2

        # # try 3 (sliding window) works
        # if len(s) == 1:
        #     return 1
        #
        # l, r = 0, 1
        # out = 0
        #
        # while r < len(s): # O(n)
        #     # print("---")
        #     # print(l, r)
        #     # print(_s)
        #
        #     _s = s[l:r] # O(n)
        #     out = max(out, len(_s))
        #
        #     if s[r] in _s: # O(n)
        #         l += _s.index(s[r]) + 1 # O(n)
        #     r += 1
        #
        #     # print("--")
        #     # print(l, r)
        #     # print(_s)
        #
        #     _s = s[l:r] # O(n)
        #     out = max(out, len(_s))
        #
        # return out
        # # time complexity: do 2n for n -> O(n^2)
        # # space complexity: _s: O(n)

        # # try 2.1
        # out = 0
        # longest = set([])
        # l, r = 0, 0
        #
        # while r < len(s):  # O(n)
        #     if s[r] in longest:  # O(1)
        #         longest.remove(s[l])
        #         l += 1
        #         continue
        #     longest.add(s[r])  # O(1)
        #     out = max(out, r - l + 1)
        #     r += 1
        #
        # return out

        # try 4 (sliding window)
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)  # ie 'ab' , l = 0, r = 1, len = 2 (1-0+1)

        return res
        # time complexity: O(n)
        # space complexity: _s: O(n)


if __name__ == "__main__":
    tests = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "b",
        " ",
        "",
        "dvdf",
    ]
    s = Solution()

    for test in tests:
        print(s.lengthOfLongestSubstring(test))
