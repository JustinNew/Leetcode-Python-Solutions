# 130. Surrounded Regions

# DFS
# Use a help matrix to label, flip, visited, or visiting.

class Solution:
    #############################################################################################################
    # maximum recursion depth exceeded in comparison
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return 

        m = len(board)
        if m == 1:
            return 
        n = len(board[0])

        help = [[0 for i in range(n)] for j in range(m)]

        def dfs(i, j):

            if board[i][j] == 'X':
                return False

            if i == 0 or i == m - 1:
                help[i][j] = 1
                return True

            if j == 0 or j == n - 1:
                help[i][j] = 1
                return True

            if help[i][j] == 0:
                help[i][j] = -1
                left = dfs(i, j - 1)
                right = dfs(i, j + 1)
                up = dfs(i - 1, j)
                down = dfs(i + 1, j)
                if left or right or up or down:
                    help[i][j] = 1
                    return True
                else:
                    board[i][j] = 'X'
                    return False
            elif help[i][j] == -1:
                return False
            else:
                return True

        for k in range(m):
            for l in range(n):
                dfs(k, l)

        return

    #######################################################################################################################
    # BFS
    def solve1(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m <= 1:
            return
        n = len(board[0]) 
        flag = [[-1 for i in range(n)] for j in range(m)]

        def bfs(i, j):
            if i - 1 > 0 and board[i - 1][j] == 'O' and flag[i - 1][j] == -1:
                flag[i - 1][j] = 1
                bfs(i - 1, j)

            if i + 1 < m and board[i + 1][j] == 'O' and flag[i + 1][j] == -1:
                flag[i + 1][j] = 1
                bfs(i + 1, j)

            if j - 1 > 0 and board[i][j - 1] == 'O' and flag[i][j - 1] == -1:
                flag[i][j - 1] = 1
                bfs(i, j - 1)

            if j + 1 < n and board[i][j + 1] == 'O' and flag[i][j + 1] == -1:
                flag[i][j + 1] = 1
                bfs(i, j + 1)

            return 

        for k in (0, m - 1):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    flag[k][l] = 1
                    bfs(k, l)

        for l in (0, n - 1):
            for k in range(m):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    flag[k][l] = 1
                    bfs(k, l)

        for k in range(m):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    board[k][l] = 'X'

        return
