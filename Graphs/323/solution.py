import unittest
from typing import List, Optional


# 1616
class Solution:
    # dfs, O(V+E)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]  # O(V), no. of nodes
        for a, b in edges:  # O(E), no. of edges
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(curr):  # O(V+E) across all calls, visit each node and edge once
            if curr in visited:
                return

            visited.add(curr)

            for n in adj[curr]:
                dfs(n)

        curr = 0
        res = 0
        while len(visited) < n:  # O(V) iterations, triggers DFS for unvisited nodes
            if curr in visited:
                curr += 1
                continue

            res += 1
            dfs(curr)

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 3
        edges = [[0, 1], [0, 2]]
        expected = 1
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        n = 6
        edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
        expected = 2
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        n = 3
        edges = [[0, 1], [0, 2], [1, 2]]
        expected = 1
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        n = 1
        edges = []
        expected = 1
        result = s.countComponents(n, edges)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
