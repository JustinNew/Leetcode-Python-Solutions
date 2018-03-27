# 63. Unique Paths II

class Solution(object):
    def uniquePathsWithObstacles(self, Grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(Grid)
        if m == 0:
            return 0 
        n = len(Grid[0])

        steps = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            if Grid[0][i] != 1 and i == 0:
                steps[0][i] = 1
            elif Grid[0][i] != 1:
                steps[0][i] = steps[0][i - 1]

        for j in range(n):
            if Grid[j][0] != 1 and j == 0:
                steps[j][0] = 1  
            elif Grid[j][0] != 1:
                steps[j][0] = steps[j - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if Grid[i][j] != 1:
                    steps[i][j] = steps[i - 1][j] + steps[i][j - 1]

        return steps[m - 1][n - 1]             
