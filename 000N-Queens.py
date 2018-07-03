# 51. N-Queens

# a function to judge whether it is a valid solution.
# n, number of queesn
# nums, the solution
# for each queen, start from the next position

import copy

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        temp = [['.' for i in range(n)] for j in range(n)]
        queens = n
        step = 0

        self.util(n, step, queens, temp, result)

        return result

    def util(self, n, step, queens, temp, result):
    
        for i in range(step, n * n):
            (ni, nj) = self.getIJ(i, n)
            if self.valid(temp, ni, nj):
                temp[ni][nj] = 'Q'
                if queens - 1 == 0:
                    saved = copy.deepcopy(temp)
                    result.append(saved)
                    return
                self.util(n, step + 1, queens - 1, temp, result)
                temp[ni][nj] = '.'

        return

    def getIJ(self, num, n):

        i = int(num / n)
        j = num - n * i

        return (i, j) 

    def valid(self, str, ni, nj):

        n = len(str)
        t = copy.deepcopy(str)
        t[ni][nj] = 'Q'

        for i in range(n):
            for j in range(n):
                if t[i][j] == 'Q':
                    # up-left
                    k, l = i - 1, j - 1
                    while k >= 0 and l >= 0:
                        if t[k][l] == 'Q':
                            return False
                        k -= 1
                        l -= 1  

                    # up-right
                    k, l = i - 1, j + 1  
                    while k >= 0 and l < n:
                        if t[k][l] == 'Q':
                            return False
                        k -= 1
                        l += 1

                    # down-left
                    k, l = i + 1, j - 1
                    while k < n and l >= 0:
                        if t[k][l] == 'Q':
                            return False
                        k += 1
                        l -= 1

                    # down-right
                    k, l = i + 1, j + 1
                    while k < n and l < n:
                        if t[k][l] == 'Q':
                            return False
                        k += 1
                        l += 1

                    # same row
                    for l in range(n):
                        if l != j and t[i][l] == 'Q':
                            return False

                    # same column
                    for k in range(n):
                        if k != i and t[k][j] == 'Q':
                            return False

        return True   

if __name__ == '__main__':

    s = Solution()
    print(s.solveNQueens(4)) 
