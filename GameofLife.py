# 289. Game of Life

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])  

        for i in range(m):
            for j in range(n):
                count = self.checkNb(i, j, board)
                if count == 3:
                    board[i][j] += 10
                elif count == 2 and board[i][j] % 10 == 1:
                    board[i][j] += 10

        for i in range(m):
            for j in range(n):
                board[i][j] = int(board[i][j] / 10)

        return 

    def checkNb(self, i, j, board):

        m = len(board)
        n = len(board[0])

        count = 0
        if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] % 10 == 1:
            count += 1
        if i - 1 >= 0 and board[i - 1][j] % 10 == 1:
            count += 1
        if j - 1 >= 0 and board[i][j - 1] % 10 == 1:
            count += 1
        if i + 1 <= m - 1 and j + 1 <= n - 1 and board[i + 1][j + 1] % 10 == 1:
            count += 1
        if j + 1 <= n - 1 and board[i][j + 1] % 10 == 1:
            count += 1
        if i + 1 <= m - 1 and board[i + 1][j] % 10 == 1:
            count += 1
        if i + 1 <= m - 1 and j - 1 >= 0 and board[i + 1][j - 1] % 10 == 1:
            count += 1
        if i - 1 >= 0 and j + 1 <= n - 1 and board[i - 1][j + 1] % 10 == 1:
            count += 1

        return count
