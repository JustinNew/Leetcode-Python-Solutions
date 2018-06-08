# 279. Perfect Squares

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        d = {}
        d[1] = 1
        d[2] = 2
        d[3] = 3

        for i in range(4, n + 1):
            if i in squares:
                d[i] = 1
            else:
                min = i
                j = len(squares) - 1
                while squares[j] > i:
                    j -= 1
                while j >= 0:
                    if 1 + d[i - squares[j]] < min:
                        min = 1 + d[i - squares[j]]
                    j -= 1
                d[i] = min

        return d[n]


# BFS.
# 1. For the first level, try all the square numbers and get the remainings.
#    For n = 12, try (1, 4, 9) and get the remainings [11, 8, 3] 
# 2. Check the next level, and get their remainings.
#    For 11, we have [10, 7, 2]
#    For 8, we have [7, 4]
#    For 3, we have [2] 
# 3. Check the next level [10, 7, 2, 7, 4, 2] -> [10, 7, 4, 2]
# 4. Continue  

def numSquares(n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp

    return cnt

if __name__ == '__main__':

    so = Solution()
    print(so.numSquares(8935)) 
