import unittest
from typing import List, Optional


class Solution:
    # dfs, time/space: O(m*n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        ROW, COL = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j):
            visited.add((i, j))
            res.append(matrix[i][j])
            up, down, left, right = (
                helper(i - 1, j),
                helper(i + 1, j),
                helper(i, j - 1),
                helper(i, j + 1),
            )
            if down and right:
                dfs(i, j + 1)
            if down and left:
                dfs(i + 1, j)
            if up and left:
                dfs(i, j - 1)
            if up and right:
                dfs(i - 1, j)

            for dr, dc in directions:
                if helper(i + dr, j + dc):
                    dfs(i + dr, j + dc)

        def helper(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COL or (i, j) in visited:
                return False
            return True

        dfs(0, 0)
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        result = s.spiralOrder(matrix)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        result = s.spiralOrder(matrix)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24],
        ]
        expected = [
            1,
            2,
            3,
            4,
            8,
            12,
            16,
            20,
            24,
            23,
            22,
            21,
            17,
            13,
            9,
            5,
            6,
            7,
            11,
            15,
            19,
            18,
            14,
            10,
        ]
        result = s.spiralOrder(matrix)
        self.assertListEqual(result, expected)

    def test4(self):
        s = Solution()
        matrix = [
            [23, 18, 20, 26, 25],
            [24, 22, 3, 4, 4],
            [15, 22, 2, 24, 29],
            [18, 15, 23, 28, 28],
        ]
        expected = [
            23,
            18,
            20,
            26,
            25,
            4,
            29,
            28,
            28,
            23,
            15,
            18,
            15,
            24,
            22,
            3,
            4,
            24,
            2,
            22,
        ]
        result = s.spiralOrder(matrix)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
