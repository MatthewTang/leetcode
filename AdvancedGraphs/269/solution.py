import unittest
from typing import Dict, List, Optional, Set
from collections import defaultdict, deque


class Solution:
    # dfs
    def foreignDictionary(self, words: List[str]) -> str:
        def dfs(char: str):
            if char in path:
                raise Exception
            if char in visited:
                return
            visited.add(char)
            path.add(char)
            for n in adj[char]:
                dfs(n)
            path.remove(char)
            top.append(char)

        if len(words) == 1:
            return words[0]

        adj = defaultdict(list)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    adj[c1].append(c2)
                    break
                j += 1
            else:
                if j < len(w1):
                    return ""

        chars = set([char for word in words for char in word])

        visited = set()
        path = set()
        top = []
        try:
            for char in chars:
                dfs(char)
        except Exception:
            return ""

        top.reverse()
        return "".join(top)

    # bfs
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        out_edges = defaultdict(list)

        in_degrees = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            j = 0
            while j < len(w1) and j < len(w2):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    out_edges[c1].append(c2)
                    in_degrees[c2] += 1
                    break
                j += 1
            else:
                if j < len(w1):
                    return ""

        q = deque([c for c in in_degrees if in_degrees[c] == 0])

        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for out_edge in out_edges[curr]:
                in_degrees[out_edge] -= 1
                if in_degrees[out_edge] == 0:
                    q.append(out_edge)

        return "".join(res) if len(res) == len(in_degrees) else ""


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        words = ["z", "o"]
        expected = "zo"
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        words = ["hrn", "hrf", "er", "enn", "rfnn"]
        expected = "hernf"
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        words = ["hrn", "hrf", "er", "enn", "rfnn", "h"]
        expected = ""
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)

    def test4(self):
        s = Solution()
        words = ["z", "z"]
        expected = "z"
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)

    def test5(self):
        s = Solution()
        words = ["wrtkj", "wrt"]
        expected = ""
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)

    def test6(self):
        s = Solution()
        words = [
            "mnop",
            "nopq",
            "opqr",
            "pqrs",
            "qrst",
            "rstu",
            "stuv",
            "tuvw",
            "uvwx",
            "vwxy",
            "wxyz",
            "xyz",
            "yz",
            "z",
            "mnopqr",
            "nopqrs",
            "opqrst",
            "pqrstu",
            "qrstuv",
            "rstuvw",
            "stuvwx",
            "tuvwxy",
            "uvwxyz",
            "vwxyz",
            "wxyza",
            "xyzab",
            "yzabc",
            "zabcd",
        ]
        expected = ""
        result = s.foreignDictionary(words)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
