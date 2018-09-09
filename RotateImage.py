# 48. Rotate Image

# Do it layer by layer.
# Be careful about clockwise or counter clockwise.
# Be careful about the indexes.

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
       
        if len(matrix) == 0:
            return

        if len(matrix) == 1:
            return

        count = len(matrix)
        l = count - 1
        i = 0
        while count >= 2:
            j = i
            for k in range(count - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l - j][i]
                matrix[l - j][i] = matrix[l - i][l - j]
                matrix[l - i][l - j] = matrix[j][l - i]
                matrix[j][l - i] = temp
                j += 1
            i += 1
            count -= 2
 
        return 

'''
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
'''
