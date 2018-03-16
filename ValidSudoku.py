# 36. Valid Sudoku
# Tedious. Careful about index.
# Valid row, column and block.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l = len(board)

        # Check each row
        for i in range(l):
            d = {}
            for j in range(l):
                t = board[i][j]
                if t >= '1' and t <= '9':
                    if t in d:
                        return False
                    else:
                        d[t] = 1
                elif t != '.':
                    return False
                
        # Check each column
        for i in range(l):
            d = {}
            for j in range(l):
                t = board[j][i]
                if t >= '1' and t <= '9':
                    if t in d:
                        return False
                    else:
                        d[t] = 1
                elif t != '.':
                    return False

        # Check each block
        for i in [0,3,6]:
            for j in [0,3,6]:
                d = {}
                for m in [0,1,2]:
                    for n in [0,1,2]:
                        t = board[i+m][j+n]
                        if t >= '1' and t <= '9':
                            if t in d:
                                return False
                            else:
                                d[t] = 1
                        elif t != '.':
                            return False

        return True
