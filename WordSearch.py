# 79. Word Search

# DFS search
# Backtrack
# Helping matrix

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        
        m = len(board)
        if m != 0:
            n = len(board[0])
        else:
            return False

        used = [[0 for i in range(n)] for j in range(m)]
        flag = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    if self.dfs(i, j, 1, board, word, used):
                        flag = 1
                    used[i][j] = 0
                if flag == 1:
                    return True

        return False

    def dfs(self, i, j, index, board, word, used):

        if index == len(word):
            return True

        if i + 1 < len(board) and board[i + 1][j] == word[index] and used[i + 1][j] == 0:
            used[i + 1][j] = 1
            if self.dfs(i + 1, j, index + 1, board, word, used):
                return True
            used[i + 1][j] = 0

        if i - 1 >= 0 and board[i - 1][j] == word[index] and used[i - 1][j] == 0:
            used[i - 1][j] = 1
            if self.dfs(i - 1, j, index + 1, board, word, used):
                return True
            used[i - 1][j] = 0

        if j + 1 < len(board[0]) and board[i][j + 1] == word[index] and used[i][j + 1] == 0:
            used[i][j + 1] = 1
            if self.dfs(i, j + 1, index + 1, board, word, used):
                return True
            used[i][j + 1] = 0

        if j - 1 >= 0 and board[i][j - 1] == word[index] and used[i][j - 1] == 0:
            used[i][j - 1] = 1
            if self.dfs(i, j - 1, index + 1, board, word, used):
                return True
            used[i][j - 1] = 0

        return False
