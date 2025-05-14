import unittest
from typing import List, Optional


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        wordDict = set(wordDict)
        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            for w in wordDict:
                if s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)

    def wordBreak(self, s: str, wordDict: List[str]):
        wordDict = set(wordDict)
        cache = {len(s): True}

        def dfs(i: int) -> bool:
            if i in cache:
                return cache[i]
            for w in wordDict:
                if s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            cache[i] = False
            return cache[i]

        return dfs(0)

    def wordBreak(self, s: str, wordDict: List[str]):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if w == s[i : i + len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "leetcode"
        wordDict = ["leet", "code"]
        expected = True
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)

    def test2(self):
        sol = Solution()
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        expected = True
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)

    def test3(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = False
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)

    def test4(self):
        sol = Solution()
        s = "catsandog"
        wordDict = ["cats", "dog", "an", "cat"]
        expected = True
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)

    def test5(self):
        sol = Solution()
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ]
        expected = False
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)

    def test6(self):
        sol = Solution()
        s = "aaaaaaa"
        expected = True
        wordDict = ["aaaa", "aaa"]
        result = sol.wordBreak(s, wordDict)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
