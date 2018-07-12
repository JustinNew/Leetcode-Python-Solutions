# 130. Surrounded Regions

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m <= 1:
            return 
        n = len(board[0])
        flag = [[-1 for i in range(n)] for j in range(m)]

        def dfs(i, j):

            if i < 0 or i >= m or j < 0 or j >= n:
                return True

            if board[i][j] == 'X':
                return False
            elif flag[i][j] == 2:
                return True
            elif flag[i][j] == 1:
                return False
            elif flag[i][j] == 0:
                return False
            elif flag[i][j] == -1:
                flag[i][j] = 0
                if dfs(i - 1, j) or dfs(i + 1, j) or dfs(i, j - 1) or dfs(i, j + 1):
                    flag[i][j] = 2
                    return True
                flag[i][j] = 1
                return False
        
        for k in range(m):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    dfs(k, l)

        for k in range(m):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == 1:
                    board[k][l] = 'X'

        return

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

if __name__ == '__main__':

    so = Solution()
    so.solve1([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
