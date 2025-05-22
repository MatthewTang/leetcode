import unittest
from typing import List, Optional


class Solution:
    # bf, time/space: O(n^2)
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        m = []
        ROW, COL = len(matrix), len(matrix[0])

        for c in range(COL):
            row = []
            for r in range(ROW - 1, -1, -1):
                row.append(matrix[r][c])
            m.append(row)

        for r in range(ROW):
            for c in range(COL):
                matrix[r][c] = m[r][c]

    # time: O(n^2), space: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            c = 0
            while c < n // 2:
                matrix[r][c], matrix[r][n - 1 - c] = matrix[r][n - 1 - c], matrix[r][c]
                c += 1

        for r in range(n):
            for c in range(n - 1 - r):
                matrix[r][c], matrix[n - 1 - c][n - 1 - r] = (
                    matrix[n - 1 - c][n - 1 - r],
                    matrix[r][c],
                )

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        r = 0
        while r < n // 2:
            matrix[r], matrix[n - 1 - r] = matrix[n - 1 - r], matrix[r]
            r += 1

        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        s.rotate(matrix)
        self.assertListEqual(matrix, expected)

    def test3(self):
        s = Solution()
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        s.rotate(matrix)
        self.assertListEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()
