# 200. Number of Islands
# Facebook Tag

# Go through each element
# Do a DFS
# Create a visited matrix

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        # Number of Rows
        m = len(grid)

        # Number of Columns
        n = len(grid[0])

        visited = [[0 for j in range(n)] for i in range(m)]

        ni = 0
        for i in range(m):

            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    ni += 1
                    self.util(i,j, m, n, grid, visited)
                if grid[i][j] == '0':
                    visited[i][j] = 1

        return ni

    def util(self, i, j, m, n, grid, visited):

        if i < 0 or i > m -1 or j < 0 or j > n - 1:
            return

        if grid[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            self.util(i-1, j, m, n, grid, visited)
            self.util(i+1, j, m, n, grid, visited)
            self.util(i, j-1, m, n, grid, visited)
            self.util(i, j+1, m, n, grid, visited)

        return
