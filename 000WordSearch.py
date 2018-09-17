# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# 'sequentially', so it is just single way without branch. 
# DFS + BackTrack + help matrix

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # 3:42
    def exist(self, board, word):
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True
        
        return False

    def getWords(self, board, word, i, j, visited, pos = 0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res

    #####################################################################################################################################
    # My own passed solution.
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

    #####################################################################################################################################
    # Time Limit Exceeded.
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0 and len(word) == 0:
            return True
        elif len(board) == 0 and len(word) != 0:
            return False

        m = len(board)
        n = len(board[0])

        visited = [[0 for i in range(n)] for j in range(m)]
        
        def search(i, j, k):
            if visited[i][j] == 0 and board[i][j] == word[k]:
                if k == len(word) - 1:
                    return True

                visited[i][j] = 1
                up = search(i - 1, j, k + 1) if i - 1 >= 0 else False
                down = search(i + 1, j, k + 1) if i + 1 < m else False
                left = search(i, j - 1, k + 1) if j - 1 >= 0 else False
                right = search(i, j + 1, k + 1) if j + 1 < n else False
                visited[i][j] = 0

                return up or down or left or right
            else:
                return False

        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True

        return False

    # Passed after change.
    def exist(self, board, word):
        if len(board) == 0 and len(word) == 0:
            return True
        elif len(board) == 0 and len(word) != 0:
            return False

        m = len(board)
        n = len(board[0])

        visited = [[0 for i in range(n)] for j in range(m)]

        def search(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i == m or j < 0 or j == n or visited[i][j] == 1 or board[i][j] != word[k]:
                return False

            visited[i][j] = 1
            res = search(i - 1, j, k + 1) or search(i + 1, j, k + 1) or search(i, j - 1, k + 1) or search(i, j + 1, k + 1)
            visited[i][j] = 0
            
            return res

        for i in range(m):
            for j in range(n):
                if search(i, j, 0):
                    return True

        return False
