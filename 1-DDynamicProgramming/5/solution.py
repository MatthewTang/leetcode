import unittest
from typing import List, Optional
from functools import lru_cache
import sys
import traceback


class Solution:
    # # time: O(3^n)
    # def longestPalindrome(self, s: str) -> str:
    #     def dfs(i: int, j: int):
    #         if i == j:
    #             return (i, j)
    #         si, sj = s[i], s[j]
    #         if si == sj:
    #             if abs(i - j) == 1:
    #                 return (i, j)
    #             else:
    #                 _i, _j = dfs(i + 1, j - 1)
    #                 if _i == i + 1 and _j == j - 1:
    #                     _i, _j = i, j
    #                 else:
    #                     _i, _j = _i, _j
    #
    #                 li, lj = dfs(i, j - 1)
    #                 ri, rj = dfs(i + 1, j)
    #                 dl = abs(li - lj)
    #                 dr = abs(ri - rj)
    #                 d_ = abs(_i-_j)
    #                 dmax = max(dl, dr, d_)
    #                 if dl == dmax:
    #                     return (li, lj)
    #                 if dr == dmax:
    #                     return (ri, rj)
    #                 else:
    #                     return (_i,_j)
    #
    #         else:
    #             li, lj = dfs(i, j - 1)
    #             ri, rj = dfs(i + 1, j)
    #             dl = abs(li - lj)
    #             dr = abs(ri - rj)
    #             if dl > dr:
    #                 return (li, lj)
    #             else:
    #                 return (ri, rj)
    #
    #     i, j = dfs(0, len(s) - 1)
    #     res = s[i : j + 1]
    #     # print(res)
    #     return res

    # # time: O(n^2)
    # def longestPalindrome(self, s: str) -> str:
    #     sys.setrecursionlimit(2000)
    #
    #     @lru_cache
    #     def dfs(i: int, j: int):
    #         if i == j:
    #             return (i, j)
    #         si, sj = s[i], s[j]
    #         if si == sj:
    #             if abs(i - j) == 1:
    #                 return (i, j)
    #             else:
    #                 _i, _j = dfs(i + 1, j - 1)
    #                 if _i == i + 1 and _j == j - 1:
    #                     _i, _j = i, j
    #                 else:
    #                     _i, _j = _i, _j
    #
    #                 li, lj = dfs(i, j - 1)
    #                 ri, rj = dfs(i + 1, j)
    #                 dl = abs(li - lj)
    #                 dr = abs(ri - rj)
    #                 d_ = abs(_i - _j)
    #                 dmax = max(dl, dr, d_)
    #                 if dl == dmax:
    #                     return (li, lj)
    #                 if dr == dmax:
    #                     return (ri, rj)
    #                 else:
    #                     return (_i, _j)
    #
    #         else:
    #             li, lj = dfs(i, j - 1)
    #             ri, rj = dfs(i + 1, j)
    #             dl = abs(li - lj)
    #             dr = abs(ri - rj)
    #             if dl > dr:
    #                 return (li, lj)
    #             else:
    #                 return (ri, rj)
    #
    #     try:
    #         i, j = dfs(0, len(s) - 1)
    #         res = s[i : j + 1]
    #         return res
    #     except Exception as e:
    #         print(e)
    #         print(sys.getrecursionlimit())
    #         print(dfs.cache_info())
    #         print(f"stack: {len(traceback.extract_tb(sys.exc_info()[2]))}")

    # # bf: O(n^3)
    # def longestPalindrome(self, s: str) -> int:
    #     # O(n)
    #     def isPalidrome(i, j) -> bool:
    #         while i < j:
    #             if s[i] == s[j]:
    #                 i += 1
    #                 j -= 1
    #             else:
    #                 return False
    #         return True
    #
    #     maxLen = 1
    #     _i, _j = 0, 0
    #     l = len(s)
    #     # O(n^2)
    #     for i in range(l):
    #         for j in range(i + 1, l):
    #             if isPalidrome(i, j):
    #                 if j - i + 1 > maxLen:
    #                     maxLen = j - i + 1
    #                     _i, _j = i, j
    #
    #     return s[_i : _j + 1] # O(n)

    # time: O(2n*n) = O(n^2)
    def longestPalindrome(self, s: str) -> int:
        l = len(s)

        # O(n)
        def _longestPalindrome(i, j):
            _i, _j = 0, 0
            while i >= 0 and j < l:
                if s[i] == s[j]:
                    _i, _j = i, j
                    i -= 1
                    j += 1
                else:
                    break
            return _i, _j

        maxLen = 1
        ri, rj = 0, 0
        # O(n), 2 iteration of j per i
        for i in range(l - 1):
            for j in range(i + 1, i + 3):
                if j < l:
                    _i, _j = _longestPalindrome(i, j)
                    if _j - _i + 1 > maxLen:
                        maxLen = _j - _i + 1
                        ri, rj = _i, _j

        return s[ri : rj + 1] # O(n)


class Test(unittest.TestCase):
    def test1(self):
        solution = Solution()
        s = "babad"
        expected = ["bab", "aba"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test2(self):
        solution = Solution()
        s = "cbbd"
        expected = ["bb"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test3(self):
        solution = Solution()
        s = "babca"
        expected = ["bab"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test4(self):
        solution = Solution()
        s = "bad"
        expected = ["b", "a", "d"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test5(self):
        solution = Solution()
        s = "b"
        expected = ["b"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test6(self):
        solution = Solution()
        s = "racecar"
        expected = ["racecar"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test7(self):
        solution = Solution()
        s = "aacabdkacaa"
        expected = ["aca"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test8(self):
        solution = Solution()
        s = "abbcccbbbcaaccbababcbcabca"
        expected = ["cbababc", "bbcccbb"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test9(self):
        solution = Solution()
        s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        expected = ["ranynar"]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)

    def test10(self):
        solution = Solution()
        s = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        expected = [
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        ]
        result = solution.longestPalindrome(s)
        self.assertTrue(result in expected)


if __name__ == "__main__":
    unittest.main()
