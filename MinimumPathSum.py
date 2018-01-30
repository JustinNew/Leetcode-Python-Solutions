# 64. Minimum Path Sum
# Dynamic Programming problem.

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0:
            return -1

        m = len(grid)
        if m == 1:
            return sum(grid[0])

        n = len(grid[0])

        steps = [[0 for i in range(n)] for j in range(m)]
        steps[0][0] = grid[0][0]

        for i in range(1,m):
            steps[i][0] = steps[i-1][0] + grid[i][0]

        for j in range(1,n):
            steps[0][j] = steps[0][j-1] + grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                steps[i][j] = min(steps[i-1][j], steps[i][j-1]) + grid[i][j]

        return steps[-1][-1]

if __name__ == '__main__':

    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
