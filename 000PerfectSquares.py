# 279. Perfect Squares

# BFS 

class Solution:

    # Top Down
    # 1. For the first level, try all the square numbers and get the remainings.
    #    For n = 12, try (1, 4, 9) and get the remainings [11, 8, 3] 
    # 2. Check the next level, and get their remainings.
    #    For 11, we have [10, 7, 2]
    #    For 8, we have [7, 4]
    #    For 3, we have [2] 
    # 3. Check the next level [10, 7, 2, 7, 4, 2] -> [10, 7, 4, 2]
    # 4. Continue

    # Time Limit Exceeded
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        squares = []
        while i * i <= n:
            squares.append(i * i)
            i += 1

        if n == squares[-1]:
            return 1

        candidates = [n]
        count = 0
        while 1:

            temp = []
            count += 1
            for v in candidates:
                for j in squares:
                    if j == v:
                        return count
                    elif j < v and v - j not in temp:
                        temp.append(v - j)

            candidates = temp 

    # Bottom up.
    # Accepted.
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        squares = []
        while i * i <= n:
            squares.append(i * i)
            i += 1
   
        if n == squares[-1]:
            return 1

        d = {i:1 for i in squares}

        while 1:

            temp = {}
            for v in d.keys():
                for j in squares:
                    if v + j == n:
                        return d[v] + 1
                    elif v + j < n:
                        temp[v + j] = d[v] + 1

            d = temp
