import unittest
from typing import List, Optional


class Solution:
    def encode(self, str: List[str]) -> str:
        # str[i].length < 200
        # list comprehension: O(len(s)) per s, hence O(sum(len(s))) = O(m)
        # .join: sum(len(s) + 3) = m + 3n = O(m+n)
        encoded = "".join([f"{len(s)+100}{s}" for s in str])
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            c = int(s[i : i + 3]) - 100
            decoded.append(s[i + 3 : i + 3 + c])
            i = i + 3 + c
        return decoded


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        input = ["neet", "code", "love", "you"]
        expected = ["neet", "code", "love", "you"]
        result = s.decode(s.encode(input))
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        input = ["we", "say", ":", "yes"]
        expected = ["we", "say", ":", "yes"]
        result = s.decode(s.encode(input))
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        input = ["we", "say", ":", "yes", "!@#$%^&*()"]
        expected = ["we", "say", ":", "yes", "!@#$%^&*()"]
        result = s.decode(s.encode(input))
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
