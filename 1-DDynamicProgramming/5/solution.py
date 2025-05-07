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

    # time: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        sys.setrecursionlimit(2000)

        @lru_cache
        def dfs(i: int, j: int):
            if i == j:
                return (i, j)
            si, sj = s[i], s[j]
            if si == sj:
                if abs(i - j) == 1:
                    return (i, j)
                else:
                    _i, _j = dfs(i + 1, j - 1)
                    if _i == i + 1 and _j == j - 1:
                        _i, _j = i, j
                    else:
                        _i, _j = _i, _j

                    li, lj = dfs(i, j - 1)
                    ri, rj = dfs(i + 1, j)
                    dl = abs(li - lj)
                    dr = abs(ri - rj)
                    d_ = abs(_i - _j)
                    dmax = max(dl, dr, d_)
                    if dl == dmax:
                        return (li, lj)
                    if dr == dmax:
                        return (ri, rj)
                    else:
                        return (_i, _j)

            else:
                li, lj = dfs(i, j - 1)
                ri, rj = dfs(i + 1, j)
                dl = abs(li - lj)
                dr = abs(ri - rj)
                if dl > dr:
                    return (li, lj)
                else:
                    return (ri, rj)

        try:
            i, j = dfs(0, len(s) - 1)
            res = s[i : j + 1]
            print(sys.getrecursionlimit())
            print(dfs.cache_info())
            print(res)
            return res
        except Exception as e:
            stack = traceback.extract_tb(sys.exc_info()[2])
            print(e)
            print(sys.getrecursionlimit())
            print(dfs.cache_info())
            print(f"depth: {len(stack)}")
            return


class Test(unittest.TestCase):
    # def test1(self):
    #     solution = Solution()
    #     s = "babad"
    #     expected = ["bab", "aba"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test2(self):
    #     solution = Solution()
    #     s = "cbbd"
    #     expected = ["bb"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test3(self):
    #     solution = Solution()
    #     s = "babca"
    #     expected = ["bab"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test4(self):
    #     solution = Solution()
    #     s = "bad"
    #     expected = ["b", "a", "d"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test5(self):
    #     solution = Solution()
    #     s = "b"
    #     expected = ["b"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test6(self):
    #     solution = Solution()
    #     s = "racecar"
    #     expected = ["racecar"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)

    # def test7(self):
    #     solution = Solution()
    #     s = "aacabdkacaa"
    #     expected = ["aca"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)
    #
    # def test8(self):
    #     solution = Solution()
    #     s = "abbcccbbbcaaccbababcbcabca"
    #     expected = ["cbababc"]
    #     result = solution.longestPalindrome(s)
    #     self.assertTrue(result in expected)

    def test9(self):
        solution = Solution()
        s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        # expected = ["cbababc"]
        result = solution.longestPalindrome(s)
        # self.assertTrue(result in expected)


if __name__ == "__main__":
    unittest.main()
