import unittest
from typing import List, Optional


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        l = {}

        for e in edges:
            a, b = e
            if a not in l:
                l[a] = [b]
            else:
                l[a].append(b)

            if b not in l:
                l[b] = [a]
            else:
                l[b].append(a)

        visited = set()

        def dfs(curr: int, prev: Optional[int]):
            if curr in visited:
                return False

            visited.add(curr)
            if not curr in l:
                return True

            neighbours = l[curr]

            for n in neighbours:
                if n == prev:
                    continue

                if not dfs(n, curr):
                    return False

            return True

        res = dfs(0, None)
        return res and len(visited) == n


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        expected = True
        result = s.validTree(n, edges)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        expected = False
        result = s.validTree(n, edges)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        n = 6
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        expected = False
        result = s.validTree(n, edges)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        edges = [[0, 1], [2, 0], [3, 0], [1, 4]]
        n = 5
        expected = True
        result = s.validTree(n, edges)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        edges = [[0, 1], [1, 3], [3, 2], [1, 4]]
        n = 5
        expected = True
        result = s.validTree(n, edges)
        self.assertIs(result, expected)

    def test6(self):
        s = Solution()
        n = 4
        edges = [[0, 1], [2, 3]]
        expected = False
        result = s.validTree(n, edges)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
