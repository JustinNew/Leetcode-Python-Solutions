# 329. Longest Increasing Path in a Matrix

# Time Limit Exceeded.
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        result = 0

        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                t = self.util(i, j, matrix)
                if t > result:
                    result = t

        return result

    def util(self, i, j, matrix):

        m = len(matrix)
        n = len(matrix[0])

        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            up = 1 + self.util(i - 1, j, matrix)
        else:
            up = 1

        if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
            down = 1 + self.util(i + 1, j, matrix)
        else:
            down = 1

        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            left = 1 + self.util(i, j - 1, matrix)
        else:
            left = 1

        if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
            right = 1 + self.util(i, j + 1, matrix)
        else:
            right = 1

        return max([up, down, left, right])

# Dynamic Programming
# dp[i][j] = max(up, down, left, right)
# Can not go by row or column number.
# Get the largest number and start from largest to smallest.

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        result = [[1 for j in range(n)] for i in range(m)]

        d = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] in d:
                    d[matrix[i][j]].append((i, j))
                else:
                    d[matrix[i][j]] = [(i, j)]

        l = [k for k, v in d.items()]
        l.sort(reverse=True)

        for num in l:
            for (i, j) in d[num]:
                m = self.util(i, j, matrix, result)
                result[i][j] += m
                        
        return max([i for sublist in result for i in sublist])

    def util(self, i, j, matrix, result):

        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            up = result[i - 1][j]
        else:
            up = 0

        if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
            down = result[i + 1][j]
        else:
            down = 0

        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            left = result[i][j - 1]
        else:
            left = 0

        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
            right = result[i][j + 1]
        else:
            right = 0

        return max([up, down, left, right])

# DP + DFS
def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))
