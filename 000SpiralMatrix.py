# 54. Spiral Matrix

# 1. Layer by layer
# Go right, down, left and up. Four directions.
# (i, j) to indicate the location of current element.
# (m, n) to indicate the steps need to go in each direction.
# Need to deal with m == 1 or n == 1 special cases.
# After one layer deal with edge case.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = 0
        result = []
        while m >= 2 and n >= 2:

            # Go Right
            for k in range(n - 1):
                result.append(matrix[i][j])
                j += 1

            # Go Down
            for k in range(m - 1):
                result.append(matrix[i][j])
                i += 1

            # Go Left
            for k in range(n - 1):
                result.append(matrix[i][j])
                j -= 1

            # Go Up
            for k in range(m - 1):
                result.append(matrix[i][j])
                i -= 1

            # Deal with edge case
            i += 1
            j += 1

            m -= 2
            n -= 2

        if m == 1:
            for k in range(n):
                result.append(matrix[i][j])
                j += 1
        elif n == 1:
            for k in range(m):
                result.append(matrix[i][j])
                i += 1

        return result

# 2. Complete eliminate one row then one column then one row then one column ...
# # Go right, down, left and up. Four directions.
# (i, j) to indicate the location of current element.
# (m, n) to indicate the steps need to go in each direction.
# There is another kind of edge case when jumped out out loop.

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = -1
        result = []

        while m >= 2 and n >= 2:

            # Go Right
            for k in range(n):
                j += 1 
                result.append(matrix[i][j])
            m -= 1
 
            # Go Down
            for k in range(m):
                i += 1
                result.append(matrix[i][j])
            n -= 1

            # Go Left
            for k in range(n):
                j -= 1
                result.append(matrix[i][j])
            m -= 1

            # Go Up
            for k in range(m):
                i -= 1
                result.append(matrix[i][j])
            n -= 1

        if m == 1:
            # Deal with edge case
            j += 1
            for k in range(n):
                result.append(matrix[i][j])
                j += 1
        elif n == 1:
            # Deal with edge case
            j += 1
            for k in range(m):
                result.append(matrix[i][j])
                i += 1 

        return result
