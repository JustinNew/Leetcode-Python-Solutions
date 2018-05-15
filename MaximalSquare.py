# 221. Maximal Square

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # Check Upper, Left and UpperLeft elements
        # If one element is Zero and itself is One, then the square size is 1
        # If all elements are One, then the largest square size is minimum of the three square size +1

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        s = [[0 for i in range(n)] for j in range(m)]
        result = 0

        for i in range(n):
            if matrix[0][i] == "1":
                s[0][i] = 1
                result = 1

        for i in range(m):
            if matrix[i][0] == "1":
                s[i][0] = 1
                result = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    if matrix[i - 1][j - 1] == "1" and matrix[i - 1][j] == "1" and matrix[i][j - 1] == "1":
                        s[i][j] = min(s[i - 1][j - 1], s[i - 1][j], s[i][j - 1]) + 1
                    else:
                        s[i][j] = 1
                    if s[i][j] > result:
                        result = s[i][j]   

        return result * result
