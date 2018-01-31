# 74. Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False

        m = len(matrix)
        n = len(matrix[0])
  
        low = 0 
        high = m * n - 1

        while low <= high:

            mid = int((high + low) / 2)
            row = int(mid / n)
            column = mid - row * n
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
