# 73. Set Matrix Zeroes
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# Use first row and first column as indicators.
# Deal with first row and column separately.

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        if len(matrix) == 0:
            return 

        m = len(matrix)
        n = len(matrix[0])

        row = 1
        column = 1

        for i in range(n):
            if matrix[0][i] == 0:
                row = 0
                break

        for i in range(m):
            if matrix[i][0] == 0:
                column = 0
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(1,m):
                    matrix[j][i] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0

        if row == 0:
            for i in range(n):
                matrix[0][i] = 0

        if column == 0:
            for i in range(m):
                matrix[i][0] = 0

        return

