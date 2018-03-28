# 96. Unique Binary Search Trees

# The number of Trees with n nodes can be reduced to 
# pick on node and construct the remaining n - 1 nodes. 

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        result = [0 for i in range(n + 1)]
        result[0] = 1
        result[1] = 1
        result[2] = 2

        for i in range(3, n + 1):
            for j in range(i):
                result[i] += result[j] * result[i - 1 - j]

        return result[-1]
