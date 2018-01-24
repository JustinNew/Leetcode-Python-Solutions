# 62. Unique Paths
# Dynamic Programming problem
# f(i,j) = f(i, j-1) + f(i-1,j)

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1

        ways = [[0 for j in range(n)] for i in range(m)]
        ways[0][0] = 1

        for i in range(m):
            for j in range(n):
                if ways[i][j] == 0:
                    if i - 1 >= 0 and j - 1 >= 0:
                        ways[i][j] = ways[i-1][j] + ways[i][j-1]
                    elif i - 1 >=0:
                        ways[i][j] = ways[i-1][j]
                    elif j - 1 >= 0:
                        ways[i][j] = ways[i][j-1]

        return ways[-1][-1]

if __name__ == '__main__':

    s = Solution()
    print (s.uniquePaths(2,2))        
