import unittest
from typing import List, Optional


class Solution:
    # # time: O(m*n*(m+n)), space: O(1)
    # def setZeroes(self, matrix) -> None:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     def setZ(i, j):
    #         for c in range(n):
    #             if matrix[i][c] != 0:
    #                 matrix[i][c] = "z"
    #
    #         for r in range(m):
    #             if matrix[r][j] != 0:
    #                 matrix[r][j] = "z"
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 setZ(i, j)
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == "z":
    #                 matrix[i][j] = 0
    #
    #     return

    # def setZeroes(self, matrix) -> None:
    #     m, n = len(matrix), len(matrix[0])
    #     zr, zc = [False] * m, [False] * n
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 zr[i] = zc[j] = True
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if zr[i] or zc[j]:
    #                 matrix[i][j] = 0

    def setZeroes(self, matrix) -> None:
        m, n = len(matrix), len(matrix[0])
        r0, c0 = False, False

        for j in range(n):
            if matrix[0][j] == 0:
                r0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                c0 = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if r0:
            for j in range(n):
                matrix[0][j] = 0

        if c0:
            for i in range(m):
                matrix[i][0] = 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        s.setZeroes(matrix)
        self.assertListEqual(matrix, expected)

    def test2(self):
        s = Solution()
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        s.setZeroes(matrix)
        self.assertListEqual(matrix, expected)

    def test3(self):
        s = Solution()
        matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
        expected = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        s.setZeroes(matrix)
        self.assertListEqual(matrix, expected)


if __name__ == "__main__":
    unittest.main()
