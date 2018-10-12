# 200. Number of Islands
# Facebook Tag

# Go through each element
# Do a BFS
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

    #############################################################################################################################
    # Maximum recursion depth exceeded in comparison

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])

        helper = [[0 for i in range(n)] for j in range(m)]
        count = 0

        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if helper[i][j] == -1:
                return
            elif helper[i][j] == 1:
                return 
            else:
                helper[i][j] = -1
                bfs(i - 1, j)
                bfs(i + 1, j)
                bfs(i, j - 1)
                bfs(i, j + 1)
                helper[i][j] = 1

                return

        for k in range(m):
            for l in range(n):
                if grid[k][l] == "1" and helper[k][l] == 0:
                    count += 1
                    bfs(k, l)

        return count


    # The BFS is not optimzed in the previous one.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])

        helper = [[0 for i in range(n)] for j in range(m)]
        count = 0

        def bfs(i, j):
            
            helper[i][j] = -1
                
            if i - 1 >= 0 and grid[i - 1][j] == "1" and helper[i - 1][j] == 0:
                bfs(i - 1, j)
            if i + 1 < m and grid[i + 1][j] == "1" and helper[i + 1][j] == 0:
                bfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == "1" and helper[i][j - 1] == 0:
                bfs(i, j - 1)
            if j + 1 < n and grid[i][j + 1] == "1" and helper[i][j + 1] == 0:    
                bfs(i, j + 1)
                    
            helper[i][j] = 1

            return

        for k in range(m):
            for l in range(n):
                if grid[k][l] == "1" and helper[k][l] == 0:
                    count += 1
                    bfs(k, l)

        return count
